from flask import Flask

app = Flask(__name__)

@app.route('/both')
def both():
    print("Printed in terminal")   # server console
    return "Shown in browser"      # browser


if __name__ == ('__main__'):
    app.run(debug=True)
