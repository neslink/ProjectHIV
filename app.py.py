from flask import Flask, render_template, request

app = Flask(__name__)

# Define the route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for handling form submission
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the form data
    borough = request.form.get('borough')

    # Perform your prediction logic here
    # (replace the following line with your actual prediction code)
    prediction_result = f"Prediction for {borough}: Positive"

    # Render the result on the main page
    return render_template('index.html', prediction=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)
