from flask import Flask, render_template
from extensions import db
from config import Config
import models
import os

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test")
def test():
    return "TrustVault is working successfully!"


if __name__ == "__main__":
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    with app.app_context():
        db.create_all()

    app.run(debug=True)