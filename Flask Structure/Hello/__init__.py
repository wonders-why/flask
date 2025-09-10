from flask import Blueprint, jsonify

hello_bp = Blueprint("hello", __name__)

#now import the routes
from Hello import routes