from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks={
        'Harry':324,
        "rohan":2354,
        'akash':235,
        'subham':235,
    }
    value=[23,marks,'keys1324']
    return jsonify(value)

app.run(debug=True)
