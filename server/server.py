from flask import Flask, request, jsonify

# create a server
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hi'

@app.route('/predict')
def predict():
    return "This house's price is 1000$"


if __name__ == "__main__":
    print("Starting Python Flask Server For Hourse Price Prediction...")
    app.run()