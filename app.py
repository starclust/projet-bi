from flask import Flask, request, jsonify, render_template
import joblib
from utils import create_features

app = Flask(__name__)
model = joblib.load("model/xgboost_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    date_str = data.get("date")
    if not date_str:
        return jsonify({"error": "Veuillez fournir une date"}), 400
    features = create_features(date_str)
    prediction = model.predict(features)[0]
    return jsonify({"date": date_str, "predicted_sales": float(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
