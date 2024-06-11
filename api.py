import json
from flask import Flask, jsonify, request
import joblib
import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def create_employee():
  transaction = json.loads(request.data)
  details = pd.DataFrame(transaction)
  model = joblib.load("random_forest_model.pkl")
  try:
    prob = model.predict_proba(details)
    return prob[0], 201
  except:
    return jsonify({ 'error': 'Invalid employee properties.' }), 400

  return '', 201, { 'location': f'/employees/{employee["id"]}' }