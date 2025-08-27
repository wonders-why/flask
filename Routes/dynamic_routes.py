from flask import Flask

app = Flask(__name__)

@app.route('/home/<name>')
def home(name):
    return f"This is a Dynamic route so we can actually use variables here like your name is {name}"
    # make sure to put the route after link http://127.0.0.1:5000/home/deepak
    

if __name__ == '__main__':
    app.run(debug=True)