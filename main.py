from server import run_server
from flask import Flask, render_template, request, session, redirect, url_for
from form import create_form, submit
from log import login
from register import register

def main():
    # Perform main program logic here
    print("Starting the server...")
    run_server()

if __name__ == '__main__':
    create_form()
    main()

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login_route():
    return login()

@app.route("/register", methods=["GET", "POST"])
def register_route():
    return register()

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "username" in session:
            # Rest of your code
        else:
            return redirect(url_for("login"))

    return render_template("form.html", submitted=False)
