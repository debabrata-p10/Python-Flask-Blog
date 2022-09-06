from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/papun")
def papun():
    return "Hello papun bhai!"

app.run (debug=True)