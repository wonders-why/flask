from flask import request, jsonify

from .services import add, subtract, multiply, divide

# Use the blueprint from __init__.py
# DO NOT import calc_bp here to avoid circular import
from . import calculator_bp  # safe only because calc_bp is already defined in __init__.py

@calculator_bp.route("/add", methods=["POST"])
def addition():
    data = request.get_json()
    nums = data.get("nums", [])
    result = add(nums)
    return jsonify({"Result": result})

@calculator_bp.route("/sub", methods=["POST"])
def subtraction():
    data = request.get_json()
    nums = data.get("nums", [])
    result = subtract(nums)
    return jsonify({"Result": result})

@calculator_bp.route("/mul", methods=["POST"])
def multiplication():
    data = request.get_json()
    nums = data.get("nums", [])
    result = multiply(nums)
    return jsonify({"Result": result})

@calculator_bp.route("/div", methods=["POST"])
def division():
    data = request.get_json()
    result, error = divide(data["a"], data["b"])
    if error:
        return jsonify({"error": error}), 400
    return jsonify({"Result": result})
