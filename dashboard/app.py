from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve input from the form
    input_data = [
        request.form['borough'],
        request.form['uhf'],
        request.form['gender'],
        request.form['age'],
        request.form['race']
    ]


    # Make predictions using the loaded model
    prediction = model.predict([input_data])

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
