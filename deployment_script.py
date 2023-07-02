from flask import Flask, request, jsonify
import joblib

# Load the saved model
model = joblib.load("model.pkl")

# Create the Flask application
app = Flask(__name__)

# Define the endpoint for model predictions
@app.route("/predict", methods=["POST"])
def predict():
    # Get the input data from the request
    data = request.json

    # Perform predictions using the loaded model
    prediction = model.predict([data])

    # Create a response dictionary
    response = {"prediction": prediction[0]}

    # Return the response as JSON
    return jsonify(response)

if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=8000)
