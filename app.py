
from flask import Flask, render_template
from flask_login import LoginManager
from config import Config
from extensions import db
from models.user import User
from routes.auth import auth_bp

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

# Flask Login Configuration
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# Register Authentication Routes
app.register_blueprint(auth_bp)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Create Database Tables
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
