import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open('hiring_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    x_test = np.array(list(data.values())).reshape(1, -1)
    if x_test.shape[1] != model.n_features_in_:
        return jsonify({"error": f"Expected {model.n_features_in_} features, but got {x_test.shape[1]} features"}), 400
    
    output = model.predict(x_test)
    print(output[0])
    return jsonify({'prediction': output[0]})

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = np.array(data).reshape(1, -1)
    print(final_input)
    output = model.predict(final_input)[0]   
    print(output)
    # Format the result for display
    if output == 1:
        prediction_text = "The person should be HIRED"
    else:
        prediction_text = "The person should NOT BE HIRED"

    # Pass the prediction result back to the template
    return render_template('home.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
