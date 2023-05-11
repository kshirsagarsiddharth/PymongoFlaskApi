from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/addnums", methods=["POST", "GET"])
def add_nums():
    data_dict = request.get_json()
    if not ('num1' in data_dict and 'num2' in data_dict):
        return {'error': 'num1 and num2 should be present in the dictonary'}
    num1 = data_dict["num1"]
    num2 = data_dict["num2"]
    return {"add": int(num1) + int(num2)},200


@app.route("/hithere")
def hi_there_everyone():
    return "Hit hithere"


@app.route("/bye")
def bye():
    age = 100 * 200
    return_json = {
        "name": "sid",
        "age": age,
        "phones": [
            {"phone_no": 1234, "phone_type": "Rts"},
            {"phone_no": 123, "phone_type": "RtsDD"},
        ],
    }

    return return_json


if __name__ == "__main__":
    app.run(debug=True)
