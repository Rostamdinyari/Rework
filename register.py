from flask import render_template, request, redirect, session, url_for

def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Registration logic (replace with your own implementation)
        if username and password:
            session["username"] = username
            return redirect(url_for("home"))

    return render_template("register.html")
