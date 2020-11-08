from lib.predict import predict
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    return "this is my flask app"


@app.route("/predict")
def predict_route():
    result = predict(request.args.get(""))
    return render_template('index.html', Title="Project")

@app.route("/user-input")
def handleUserInput():
    userInput = request.args.get("sentence")
    print(userInput)
    return None
