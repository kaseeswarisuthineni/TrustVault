
from flask import Blueprint, render_template, request
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models.user import User

auth_bp = Blueprint("auth", __name__)


# User Registration
@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return "Email already registered"

        hashed_password = generate_password_hash(password)

        new_user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return "Registration successful!"

    return render_template("register.html")


# User Login
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            login_user(user)

            return "Login successful!"

        return "Invalid email or password"

    return render_template("login.html")
