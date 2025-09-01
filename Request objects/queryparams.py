#Importing modules
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

link = r"C:\The Sorcerer’s Script\Flask\Flask code\Request objects\people.json"


#Loading the file using file handlling and json 
def load_data():
    with open(link, "r") as file:
       return json.load(file)


@app.route('/search')
def search():
    data = load_data()
    Name = request.args.get('name')
    City = request.args.get('city')

    result = [] #it is an empty list that will store the data based on incoming data

    #now lets get the data realted to the parameters like name and city.
    for user in data["users"]:
        if Name and str(user["name"]).lower() != str(Name).lower():
            continue
        if City and str(user["city"]).lower()!= str(City).lower():
            continue
        result.append(user)
    return jsonify({"Result": result})


if __name__ == '__main__':
    app.run(debug=True)