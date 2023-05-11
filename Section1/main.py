from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/hithere")
def hi_there_everyone():
    return "Hit hithere"


@app.route("/bye")
def bye():
    age = 100 * 200 
    return_json = {
        "name": "sid",
        "age": age,
        "phones": [{"phone_no": 1234, "phone_type": "Rts"},{"phone_no": 123, "phone_type": "RtsDD"}],
    }

    return return_json


if __name__ == "__main__":
    app.run(debug=True)
