from flask import Flask, request, jsonify, abort
import json
import os

app = Flask(__name__)

# -----------------------------
# File handling
# -----------------------------
link = "users.json"

def load_data():
    if not os.path.exists(link):
        return {"users": []}
    with open(link, "r") as file:
        return json.load(file)

def dump_to_json(payload):
    with open(link, "w") as file:
        json.dump(payload, file, indent=4)

# -----------------------------
# Routes
# -----------------------------
@app.route('/user', methods=['POST'])
def create_user():
    try:
        payload = request.get_json()

        # Input validation
        if not payload:
            return jsonify({"error": "Missing JSON body"}), 400
        required_fields = ["id", "name", "email", "role"]
        missing_fields = [f for f in required_fields if f not in payload]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        if not isinstance(payload["id"], int):
            return jsonify({"error": "'id' must be an integer"}), 400
        if not isinstance(payload["name"], str) or len(payload["name"]) < 2:
            return jsonify({"error": "'name' must be a string of at least 2 characters"}), 400
        if "@" not in payload["email"]:
            return jsonify({"error": "Invalid email format"}), 400

        data = load_data()

        # Check if user exists
        for user in data["users"]:
            if user["id"] == payload["id"]:
                abort(400, description="User already exists")

        data["users"].append(payload)
        dump_to_json(data)
        return jsonify({"message": "User created successfully", "user": payload}), 201

    except Exception as e:
        # Catch-all exception handler
        return jsonify({"error": f"Server error: {str(e)}"}), 500

# Example GET route
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    data = load_data()
    for user in data["users"]:
        if user["id"] == user_id:
            return jsonify(user)
    abort(404, description="User not found")

# -----------------------------
# HTTP-specific error handlers
# -----------------------------
@app.errorhandler(400)
def handle_400(error):
    return jsonify({"error": str(error.description), "status_code": 400}), 400

@app.errorhandler(404)
def handle_404(error):
    return jsonify({"error": str(error.description), "status_code": 404}), 404

@app.errorhandler(500)
def handle_500(error):
    return jsonify({"error": "Internal server error", "status_code": 500}), 500

# -----------------------------
# Run the app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
