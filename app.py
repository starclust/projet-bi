from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Charger le modèle
model = joblib.load('modele_delai_paiement.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données
        if request.is_json:
            data = request.get_json()
            invoice_amount = float(data.get('InvoiceAmount', 0))
            discount_offered = float(data.get('DiscountOffered', 0))
            discount_used = float(data.get('DiscountUsed', 0))
        else:
            invoice_amount = float(request.form.get('InvoiceAmount', 0))
            discount_offered = float(request.form.get('DiscountOffered', 0))
            discount_used = float(request.form.get('DiscountUsed', 0))

        # Préparer les features
        features = np.array([[invoice_amount, discount_offered, discount_used]])

        # Prédire
        prediction = model.predict(features)
        result = max(round(float(prediction[0]), 2), 0)  # Le délai ne peut pas être négatif

        if request.is_json:
            return jsonify({"prediction": result})
        else:
            return render_template('index.html', prediction_text=f"Délai de paiement prédit : {result} jours")

    except Exception as e:
        error_message = f"Erreur lors de la prédiction : {str(e)}"
        if request.is_json:
            return jsonify({"error": error_message}), 400
        return render_template('index.html', prediction_text=error_message)

if __name__ == '__main__':
    app.run(debug=True)
