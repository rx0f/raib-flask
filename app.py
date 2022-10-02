from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tryit")
def tryit():
    return render_template("tryit.html")

@app.route("/model", methods=["POST"])
def model():
    text = request.form['link']
    return redirect("/tryit")