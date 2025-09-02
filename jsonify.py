#While building api's the format user expects data is mostly in json so tahts why flask provides us a method called jsonify to send data in json format.

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def post_user():
    user = {"name" : "deepak", "age" : 20, "course" : "bca"}
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)

#OUTPUT
{
  "name": "deepak",
  "age": 20,
  "course": "bca"
}
