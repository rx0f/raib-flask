from flask import Flask, render_template, request, redirect
from os import system

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tryit")
def tryit():
    return render_template("tryit.html")

@app.route("/display")
def display():
    return render_template("display.html")

@app.route("/model", methods=["POST"])
def model():
    
    link = request.form['link']
    if link.startswith("https://www.missionjuno.swri.edu/junocam/processing?id="):
        if link.startswith("https://www.missionjuno.swri.edu/junocam/processing?id=JNCE_2019149_"):
            system(f"py model.py {link}")
            return redirect("/display")
        else:
            return redirect("/tryit")
    else:
        return redirect("/tryit")
    