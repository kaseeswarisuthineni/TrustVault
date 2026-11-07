import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from extensions import db
from models.document import Document

documents_bp = Blueprint("documents", __name__)

ALLOWED_EXTENSIONS = {"pdf", "doc", "docx", "txt", "png", "jpg", "jpeg"}

@documents_bp.route("/upload", methods=["GET", "POST"])
@login_required
def upload():

    if request.method == "POST":

        file = request.files.get("document")

        if not file or file.filename == "":
            flash("Please select a file")
            return redirect(url_for("documents.upload"))

        filename = secure_filename(file.filename)

        extension = filename.rsplit(".", 1)[-1].lower()

        if "." not in filename or extension not in ALLOWED_EXTENSIONS:
            flash("File type not allowed")
            return redirect(url_for("documents.upload"))

        upload_folder = current_app.config["UPLOAD_FOLDER"]
        os.makedirs(upload_folder, exist_ok=True)

        file_path = os.path.join(upload_folder, filename)

        file.save(file_path)

        document = Document(
            filename=filename,
            file_path=filename,
            owner_id=current_user.id
        )

        db.session.add(document)
        db.session.commit()

        flash("File uploaded successfully!")

    return render_template("upload.html")