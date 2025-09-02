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
        users = load_data()  # may raise FileNotFoundError or JSONDecodeError
        for user in users:
            if user["id"] == user_id:
                return jsonify(user)
        abort(404, description="User doesn't exist")
    
    except FileNotFoundError:
        return jsonify({"error": "Database file not found"}), 500
    
    except json.JSONDecodeError:
        return jsonify({"error": "JSON file is invalid"}), 500

if __name__ == "__main__":
    app.run(debug=True)
