from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    # 1️⃣ Check if JSON body exists
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    # 2️⃣ Check required fields
    required_fields = ["id", "name", "email", "role"]

    
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

    # 3️⃣ Check types
    if not isinstance(data["id"], int):
        return jsonify({"error": "'id' must be an integer"}), 400
    if not isinstance(data["name"], str):
        return jsonify({"error": "'name' must be a string"}), 400
    if not isinstance(data["email"], str):
        return jsonify({"error": "'email' must be a string"}), 400
    if not isinstance(data["role"], str):
        return jsonify({"error": "'role' must be a string"}), 400

    # 4️⃣ Check value constraints (optional)
    if data["id"] <= 0:
        return jsonify({"error": "'id' must be positive"}), 400
    if len(data["name"]) < 2:
        return jsonify({"error": "'name' must be at least 2 characters"}), 400

    # 5️⃣ Optional: Validate email format (basic)
    if "@" not in data["email"]:
        return jsonify({"error": "Invalid email format"}), 400

    # If all validations pass
    return jsonify({"message": "Validation passed!", "user": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
