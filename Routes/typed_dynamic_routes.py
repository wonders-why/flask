from flask import Flask

app = Flask(__name__)

@app.route('/<int:degits>')
def home(degits):
    return f"This is a typed dynamic funtion so we can actually decide the type of input we take, like int, string, double or a path which consists of names with slash.for example you wont be able to enter a string in this one. the degits u enter are {degits}"

if __name__ == '__main__':
    app.run(debug=True)