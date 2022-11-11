from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.workout import Workout
from flask import flash



# ========================= LOG IN & REGISTRATION PAGE (1) ======================
@app.route("/")
def index():
    return render_template("index.html")


# ========================= WELCOME PAGE (2) ====================================

@app.route("/welcome")
def welcome_page():
    return render_template("welcome.html")

# ========================= PATH DECISION PAGE (3) ==============================

@app.route("/welcome_path")
def welcome():
    return render_template("welcome_path.html")





# ========================= REGISTRATION PROCESS ================================

@app.route("/register", methods=["POST"])
def register():
    valid_user = User.create_valid_user(request.form)

    if not valid_user:
        return redirect("/")
    
    session["user_id"] = valid_user.id
    
    return redirect("/welcome")


# ========================= LOGIN PROCESS ======================================

@app.route("/login", methods=["POST"])
def login():
    valid_user = User.authenticated_user_by_input(request.form)
    
    if not valid_user:
        return redirect("/")

    session["user_id"] = valid_user.id
    return redirect("/welcome")


# ========================= LOGOUT PROCESS  ====================================

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")




