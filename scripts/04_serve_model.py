from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)