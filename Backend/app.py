from flask_cors import CORS
from flask import Flask, request, jsonify
import pickle
import pandas as pd

# create app
app = Flask(__name__)
CORS(app)

# load model
model = pickle.load(open('model.pkl', 'rb'))

# home route
@app.route('/')
def home():
    return "Crop Recommendation API is running"

# prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # convert input into DataFrame
    sample = pd.DataFrame([[ 
        data['N'], data['P'], data['K'],
        data['temperature'], data['humidity'],
        data['ph'], data['rainfall']
    ]], columns=['N','P','K','temperature','humidity','ph','rainfall'])

    prediction = model.predict(sample)

    return jsonify({
        'recommended_crop': prediction[0]
    })

# run server
    import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))