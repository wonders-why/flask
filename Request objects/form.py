#importing modules
from flask import Flask, request, jsonify
import json

app = Flask('__name__')

link = r"C:\The Sorcerer’s Script\Flask\Flask code\Request objects\formpassword.json"

def load_data():
    with open(link, "r") as file:
        return json.load(file)

@app.route('/form', methods = ['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
            return jsonify({"Error" : "Please enter the Username and Password"}),404

    data = load_data()
    
    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            return jsonify({"Message" : "Successfully logged In!"}),200
    return jsonify({"Error":"Enter the right password"}),400



if __name__ == '__main__':
    app.run(debug=True)