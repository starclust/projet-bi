from flask import Flask, request, render_template, jsonify
import torch
import torch.nn as nn
import joblib
import numpy as np

app = Flask(__name__)

# Modèle de recommandation (Matrix Factorization)
class MatrixFactorization(nn.Module):
    def __init__(self, n_users, n_items, embedding_dim=30):
        super(MatrixFactorization, self).__init__()
        self.user_emb = nn.Embedding(n_users, embedding_dim)
        self.item_emb = nn.Embedding(n_items, embedding_dim)

    def forward(self, user, item):
        user_vec = self.user_emb(user)
        item_vec = self.item_emb(item)
        return (user_vec * item_vec).sum(1)

# Chargement des encoders et du modèle
client_enc = joblib.load("mf_client_encoder.pkl")
product_enc = joblib.load("mf_product_encoder.pkl")
n_users = len(client_enc.classes_)
n_items = len(product_enc.classes_)

model = MatrixFactorization(n_users, n_items)
model.load_state_dict(torch.load("mf_model.pth"))
model.eval()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    client_id = request.form['client_id']
    try:
        client_idx = client_enc.transform([client_id])[0]
    except:
        return render_template('index.html', error="Client non trouvé.")

    user_tensor = torch.tensor([client_idx] * n_items)
    item_tensor = torch.tensor(range(n_items))

    with torch.no_grad():
        scores = model(user_tensor, item_tensor)

    top_k = torch.topk(scores, k=5)
    recommended_idxs = top_k.indices.numpy()
    recommended_products = product_enc.inverse_transform(recommended_idxs)
    recommended_products = recommended_products.tolist()  # ✅ Ajout essentiel

    return render_template('index.html', client_id=client_id, recommendations=recommended_products)

if __name__ == '__main__':
    app.run(debug=True)
