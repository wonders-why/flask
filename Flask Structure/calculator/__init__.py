from flask import Blueprint

calculator_bp = Blueprint("calculator", __name__)#The blue print is created now

from calculator import routes