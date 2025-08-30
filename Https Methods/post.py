#initializing libraries
from flask import Flask, jsonify, request
import json
import os

#creating the app
app = Flask(__name__)

#link
link = "users.json"

#loading the data
def load_data():
    with open(link, "r")as file:
        return json.load(file) 

#dumping the data 
def dump_to_json(Payload):
    with open(link, "w")as file:
        json.dump(Payload, file, indent=4)



@app.route('/user', methods = ['POST'])
def post_data():
    payload = request.get_json()
    data = load_data()
    #running the loop to check if user exists
    for user in data["users"]:
        if str(user['id']) == str(payload['id']):
            return jsonify({"Message" : "The user already exists"}),400     
    
    data['users'].append(payload)
    dump_to_json(data)
    return jsonify({"Messgae" :"The data is successfully saved."}),201




#running the app
if __name__ =="__main__":
    app.run(debug=True)