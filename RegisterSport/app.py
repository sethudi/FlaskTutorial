from flask import Flask, render_template, request

app = Flask(__name__)

SPORT = ["Basketball", "Soccer", "Ultimate Frisbee"]

@app.route("/")
def index():
    return render_template("index.html", sports =SPORT)


@app.route("/register", methods =["POST"])  
def register():
    if not request.form.get("name") and not request.form.get("sport"):
        return render_template("failure.html")
    return render_template("success.html")
