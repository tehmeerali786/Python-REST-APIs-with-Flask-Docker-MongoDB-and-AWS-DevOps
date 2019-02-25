from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def checkPostedData(postedData, functionName):
    if (functionName == "add"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200

class Add(Resource):
    def post(self):
        # If I am here, then the resource Add was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Step 1b: Verify validity of
        status_code = checkPostedData(postedData, "add")
        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code

            }

            return jsonify(retJson)



        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)


        #Step 2: Add the posted data
        ret = x+y
        retMap = {

            "Message" : ret,
            "Status Code" : 200
        }

        return jsonify(retMap)



class Subtract(Resource):
    pass

class Multiply(Resource):
    pass


class Divide(Resource):
    pass


api.add_resource(Add, "/add")



if __name__ == "__main__":
    app.run(debug = True)
