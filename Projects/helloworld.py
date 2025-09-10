#importing modules
from flask import Flask, jsonify
import datetime

#ceating the app
app = Flask(__name__)

#the funtion of program is to send hellow world as json on the site so lets do it...

#creating a def followed by a route
@app.route("/hello/<user_name>")
def Greet(user_name):
    time = datetime.datetime.now().hour
    if time > 12:
        greeting = "Morning"
    elif time < 12 and time >= 16:
        greeting = "afternoon"
    elif time >= 17 and time < 21:
        greeting = "Evening"
    else:
        greeting = "Night"

    return jsonify({"Message" : f"Good {greeting}, {user_name}"})



#running the app
if __name__ == "__main__":
    app.run(debug=True)
