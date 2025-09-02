#example of 404
from flask import Flask, jsonify

app = Flask(__name__)

# Custom 404 handler
@app.errorhandler(404)
def handle_404(error):
    return jsonify({"error": "Resource not found", "status_code": 404}), 404
#custom 500 handler
@app.errorhandler(500)
def handle_500(error):
    return jsonify({"error": "Something went wrong on the server!", "status_code": 500}), 500

# Example route
@app.route('/user/<int:user_id>')
def get_user(user_id):
    # Imagine you have no users
    return jsonify({"message": "This is a demo"}), 200

if __name__ == "__main__":
    app.run(debug=True)
