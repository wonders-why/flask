from flask import Flask as fk

app = fk(__name__)

@app.route('/')
def home():
    return "Hello, Nigga money"

if __name__ == '__main__':
    app.run(debug=True)