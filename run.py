from lib.predict import predict
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predict")
def predict_route():
    sentence = request.args.get("sentence")
    output = predict(sentence)
    if output == 1:
        output = "Positive"
    else:
        output = "Negative"
    return render_template('index.html', result=output, sentence=sentence, showPrediction=True)


app.run( port="3000", debug=True)