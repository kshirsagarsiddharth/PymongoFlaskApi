from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def check_posted_data(posted_data, function_name):
    try: 
        if (
            function_name == "add"
            or function_name == "subtract"
            or function_name == "multiply"
            or function_name == "divide"
        ):
            if "x" not in posted_data or "y" not in posted_data:
                return 301
            elif int(posted_data["y"]) == 0:
                return 302
            else:
                return 200
    except ValueError as e: 
        return 304 


class Add(Resource):
    def post(self):
        # if i am here then the resource add was requested using the method POST

        # step 1: get posted data
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, "add")
        if status_code != 200:
            return {"Message": "An error occured", "status": status_code}
        x = posted_data["x"]
        y = posted_data["y"]
        x, y = int(x), int(y)

        return {"sum": x + y, "status": 200}


class Subtract(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, "subtract")
        if status_code != 200:
            ret_json = {"message": "An error occured", "status code": status_code}
            return ret_json

        x, y = int(posted_data["x"]), int(posted_data["y"])
        ret_map = {"message": x - y, "status code": 200}

        return ret_map


class Multiply(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, "multiply")
        if status_code != 200:
            ret_json = {"message": "An error occured", "status code": status_code}
            return ret_json

        x, y = int(posted_data["x"]), int(posted_data["y"])
        ret_map = {"message": x * y, "status code": 200}

        return ret_map


class Divide(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, "divide")
        if status_code != 200:
            ret_json = {"message": "An error occured", "status code": status_code}
            return ret_json

        x, y = int(posted_data["x"]), int(posted_data["y"])

        ret_map = {"message": x / y, "status code": 200}

        return ret_map


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/sub")
api.add_resource(Multiply, "/mul")
api.add_resource(Divide, "/div")

if __name__ == "__main__":
    app.run(debug=True)
