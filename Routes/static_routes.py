from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "This is a normal static funtion with no changes and flexibility or interactivity"

if __name__ == '__main__':
    app.run(debug=True)