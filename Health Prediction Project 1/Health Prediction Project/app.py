from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the pre-trained KNN model
with open("model.pkl", "rb") as file:
    knn_model = pickle.load(file)

# Load the dataset
data = pd.read_csv('heart.csv')

# Define numerical columns
numerical_cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# Create and fit the scaler
scaler = StandardScaler()
scaler.fit(data[numerical_cols])

# Homepage with a form for user input
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/#')
def about():
    return render_template('#')

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve user input from the form
        input_data = {col: [float(request.form[col])] for col in numerical_cols}
        input_df = pd.DataFrame(input_data)

        # Preprocess the input data
        input_scaled = scaler.transform(input_df)

        # Make prediction
        prediction = knn_model.predict(input_scaled)

        # Return prediction result
        if prediction[0] == 0:
            result = "No Heart Disease"
        else:
            result = "Heart Disease Detected"

        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
