from flask import Flask
from lib.predict import predict
app = Flask(__name__)


@app.route("/")
def index():
    return "this is my flask app"


@app.route("/predict")
def predict_route():
    result = predict(request.args.get(""))
