#Inistialising modules
from flask import Flask, request, jsonify
import json

#Creating the app
app = Flask(__name__)

#link to the json
link = "users.json"

#json loader
def load_json():
    with open(link, 'r')as file:
        return json.load(file)

#json dumper
def dump_json(data):
    with open(link, "w")as file:
        json.dump(data, file, indent=4)

#the first thiing is i have to check  if the data exists already and if it doesnt then i will replace it. 
#if it doesnt i have hardcode what i want to do create or throw error

@app.route('/users', methods =['PUT'])
def update_data():
    #Storing the data
    data = load_json()
    Payload = request.get_json()

    Updated = False

    #looping through the data
    for user in data["users"]:
        if str(user["id"]) == str(Payload["id"]):
            user.update(Payload)#update funtion of dicts used here to append this is the core

            Updated = True
            break   
    if Updated == True:
        dump_json(data)
        return jsonify({"Message" :"The User is updated succesfully!"}),201
    elif Updated == False:
        return jsonify({"Message" : "The user doesnt exist!"}),404

#updating the json file


#running the app
if __name__ == '__main__':
    app.run(debug=True)