from flask import Flask, redirect

app = Flask(__name__)

@app.route('/damn')
def damn():
    return redirect("https://www.google.com")
    #return redirect(url_for('https://www.google.com'))
    #the url for only works for an internal templete 
if __name__ == '__main__':
    app.run(debug=True)