#libraries 
from flask import Flask, request, jsonify
import json

#Making the app
app = Flask(__name__)

#link to file 
link = "users.json"

#Loading the file using file handlling and json 
def load_data():
    with open(link, "r") as file:
       return json.load(file)

#A all adata route
@app.route('/users')
def get_users():
    payload = load_data()
    return jsonify(payload["users"])


#createing a simple route
@app.route('/users/<user_id>', methods = ['GET'])

#a funtion followed by the route
def get_data(user_id):
    payload = load_data()
    for user in payload["users"]:
        if str(user['id']) == str(user_id):
            return jsonify(user)
    return jsonify({"Message" : "The user does'nt Exist"}),404


#saving the data in the file
def save_data(payload):
    with open(link, "w") as file:
        json.dump(payload, file, indent=4)

#running the application 
if __name__ == '__main__':
    app.run(debug=True)


#this shit took the toal out of me bruh im sooo devastated