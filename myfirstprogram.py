from flask import Flask as fk

app = fk(__name__) #creates a flask app instance

@app.route('/') #maps the root url / to the home funtion

def home():
    return "Hello, Nigga money"

if __name__ == '__main__':
    app.run(debug=True) #enables auto reload and error debugging...