from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Charger le modèle
model = joblib.load('modele_delai_paiement.joblib')

# Définir le pourcentage qu'on veut prendre
PERCENTAGE = 0.30  # 30%

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

        # Normalisation
        invoice_amount /= 1000
        discount_offered /= 100
        discount_used /= 100

        # Préparer les features
        features = np.array([[invoice_amount, discount_offered, discount_used]])

        # Prédire
        prediction = model.predict(features)
        days = max(round(float(prediction[0]), 0), 0)  # Résultat en jours
        months = max(int(days / 30), 0)  # Transformer en mois entiers

       
        adjusted_months = max(int(months * PERCENTAGE), 1) 
        if request.is_json:
            return jsonify({"predicted_payment_delay_months": adjusted_months})
        else:
            return render_template('index.html', prediction_text=f"Predicted payment delay: {adjusted_months} months")

    except Exception as e:
        error_message = f"Error during prediction: {str(e)}"
        if request.is_json:
            return jsonify({"error": error_message}), 400
        return render_template('index.html', prediction_text=error_message)

if __name__ == '__main__':
    app.run(debug=True)
