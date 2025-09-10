from . import hello_bp
from flask import jsonify, request

@hello_bp.route("/Greet/<username>", methods = ["GET"])
def hello(username):
    return jsonify({"Message":f"Konnichiwa, Mr {username}"})