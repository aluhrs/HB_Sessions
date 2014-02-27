from flask import Flask, render_template, request, redirect, url_for, session, flash
import model

app = Flask(__name__)
app.secret_key = "shhhhthisisasecret"

@app.route("/")
def index():
    if session.get("username"):
        return redirect(url_for("view_user", username=session['username']))
        #render_template("loggedin.html", username=session['username'])
        #"User %s is logged in!" % session['username']
    else:
        return render_template("index.html")

@app.route("/", methods=["POST"])
def process_login():
    username = request.form.get("username")
    password = request.form.get("password")
    model.connect_to_db()
    user_id = model.authenticate(username, password)

    if user_id != None:
        flash("User authenticated")
        session['user_id'] = user_id
        session['username'] = username
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

@app.route("/user/<username>")
def view_user(username):
    model.connect_to_db()
    user_id = model.get_user_by_name(username)
    wall_posts = model.get_wallposts_by_userid(user_id)
    return render_template("wall.html", wall_posts=wall_posts, username=username)


if __name__ == "__main__":
    app.run(debug = True)
