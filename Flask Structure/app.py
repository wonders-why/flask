from flask import Flask
from Hello import hello_bp
from calculator import calculator_bp
app = Flask(__name__)

# Register blueprint

app.register_blueprint(hello_bp)
app.register_blueprint(calculator_bp)
if __name__ == "__main__":
    app.run(debug=True)
