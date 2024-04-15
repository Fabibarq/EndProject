from flask import Flask, request, jsonify
import numpy as np
from model import model

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array(data['features'][:8]).reshape(1, -1)  # Tomar solo las primeras 8 características
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
