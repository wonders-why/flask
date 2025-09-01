#Importing modules
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

link = "users.json"

#funtion to load data
def load_json():
    with open(link, "r")as file:
        return json.load(file)
    
#funtion to upload data
def update_data(data):
    with open(link, "w")as file:
        json.dump(data, file, indent=4)

@app.route("/user", methods=['DELETE'])
def delete_user():
    data = load_json()
    payload = request.get_json()

    #loop to check if the user exists so we can delete him
    for user in data["users"]:
        if str(user["id"]) == str(payload["id"]):
            data["users"].remove(user)
            update_data(data)
            return jsonify({"Messsage" : "The user is deleted"}),201
    return jsonify({"Message" :"The user doesnt exist"}),404





if __name__ == '__main__':
    app.run(debug=True)
