from flask import Flask, jsonify, abort
import json

app = Flask(__name__)

link = "usersforabort.json"

def load_data():
    with open(link, 'r') as file:
        return json.load(file)
    
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        users = load_data()  # access the "users" key

        for user in users:
            if user["id"] == user_id:
                return jsonify(user)

    # If we finish loop without returning, user not found
        abort(404, description="User doesn't exist")
        
    except FileNotFoundError:
        return jsonify({"Error" : "File not found!"})
    except json.JSONDecodeError:
        return jsonify({"Error" : "Wrong format of json"})

if __name__ == "__main__":
    app.run(debug=True)
