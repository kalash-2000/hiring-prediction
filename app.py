import pickle
from flask import Flask, request, app, jsonify, url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
#load the model
model = pickle.load(open('salary_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data = request.json['data']
    print(data)
    x_test =  np.array(list(data.values())).reshape(1,-1)
    if x_test.shape[1] != model.n_features_in_:
        return jsonify({"error": f"Expected {model.n_features_in_} features, but got {x_test.shape[1]} features"}), 400
    
    output = model.predict(x_test)
    print(output[0])
    result = float(output[0])
    return str(output[0])

if __name__ == "__main__":
    app.run(debug=True)