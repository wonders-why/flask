#importing modules
from flask import Flask, jsonify, request
#ceating the app
app = Flask(__name__)

#Caculator api 
#creating multliple routes for each Operation
@app.route("/add", methods = ['POST'])
def addition():
    data = request.get_json()
    numbers = data.get("nums", [])
    result = numbers[0]
    for num in numbers[1:]:
        result += num
    return jsonify({"Result" : result})


@app.route("/sub", methods = ['POST'])
def subtract():
    data = request.get_json()
    numbers = data.get("nums", [])
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return jsonify({"Result" : result})


@app.route("/mul", methods = ['POST'])
def multiply():
    data = request.get_json()
    numbers = data.get("nums", [])
    result = numbers[0]
    for num in numbers[1:]:
        result *= num
    return jsonify({"Result" : result})


@app.route("/div", methods = ['POST'])
def divide():
    data = request.get_json()
    if data["b"] == 0:
        return jsonify({"error" : "Enter a valid value"}),400
    result = data["a"] / data["b"]
    return jsonify({"Result" : result})



#running the app
if __name__ == "__main__":
    app.run(debug=True)
