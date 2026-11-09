import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Create required folders if they do not exist
DATABASE_DIR = os.path.join(BASE_DIR, "database")
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

os.makedirs(DATABASE_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)


class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "trustvault-local-key"
    )

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + os.path.join(
            DATABASE_DIR, "trustvault.db"
        )
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = UPLOAD_DIR

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024