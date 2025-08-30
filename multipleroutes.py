from flask import Flask

app = Flask(__name__)

@app.route('/')   # homepage
def home():
    return "This is the Home Page"

@app.route('/about')   # about page
def about():
    return "This is the About Page"

@app.route('/contact')   # contact page
def contact():
    return "This is the Contact Page"

if __name__ == '__main__':
    app.run(debug=True)