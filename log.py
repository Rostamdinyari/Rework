from flask import render_template, request, redirect, session, url_for

def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Login validation logic (replace with your own implementation)
        if username == "admin" and password == "password":
            session["username"] = username
            return redirect(url_for("home"))

    return render_template("login.html")
