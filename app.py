from flask import Flask, render_template, request, redirect, url_for, session, flash
import model

app = Flask(__name__)
app.secret_key = "shhhhthisisasecret"

@app.route("/")
def index():
    if session.get("username"):
        return render_template("loggedin.html", username=session['username'])
        #"User %s is logged in!" % session['username']
    else:
        return render_template("index.html")

@app.route("/", methods=["POST"])
def process_login():
    username = request.form.get("username")
    password = request.form.get("password")

    username = model.authenticate(username, password)

    if username != None:
        flash("User authenticated")
        session['username'] = username
        print session['username']
    else:
        flash("Password incorrect, there may be a ferret stampede in progress!")

    return redirect(url_for("index"))    

    #return render_template("login.html")

@app.route("/close")
def end_session():
    session.clear()

    return redirect(url_for("index"))

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug = True)
