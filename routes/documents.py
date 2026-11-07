import os
import uuid

from flask import (
    Blueprint, render_template, request,
    redirect, url_for, flash,
    current_app, send_from_directory
)

from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from extensions import db
from models.document import Document

documents_bp = Blueprint("documents", __name__)

ALLOWED_EXTENSIONS = {
    "pdf", "doc", "docx", "txt",
    "png", "jpg", "jpeg"
}

MAX_FILE_SIZE = 16 * 1024 * 1024


# Upload Document
@documents_bp.route("/upload", methods=["GET", "POST"])
@login_required
def upload():

    if request.method == "POST":

        file = request.files.get("document")

        if not file or file.filename == "":
            flash("Please select a file")
            return redirect(url_for("documents.upload"))

        filename = secure_filename(file.filename)

        if "." not in filename:
            flash("Invalid file name")
            return redirect(url_for("documents.upload"))

        extension = filename.rsplit(".", 1)[1].lower()

        if extension not in ALLOWED_EXTENSIONS:
            flash("File type not allowed")
            return redirect(url_for("documents.upload"))

        # Check file size
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        file.seek(0)

        if file_size > MAX_FILE_SIZE:
            flash("File size must be less than 16 MB")
            return redirect(url_for("documents.upload"))

        upload_folder = current_app.config["UPLOAD_FOLDER"]
        os.makedirs(upload_folder, exist_ok=True)

        # Generate unique filename
        unique_filename = str(uuid.uuid4()) + "." + extension

        # Save file
        file.save(os.path.join(upload_folder, unique_filename))

        # Save document details
        document = Document(
            filename=filename,
            file_path=unique_filename,
            owner_id=current_user.id
        )

        db.session.add(document)
        db.session.commit()

        flash("File uploaded successfully!")

        return redirect(url_for("documents.upload"))

    return render_template("upload.html")


# View Documents
@documents_bp.route("/documents")
@login_required
def view_documents():

    documents = Document.query.filter_by(
        owner_id=current_user.id
    ).all()

    return render_template(
        "documents.html",
        documents=documents
    )


# Download Document
@documents_bp.route("/download/<int:document_id>")
@login_required
def download_document(document_id):

    document = Document.query.filter_by(
        id=document_id,
        owner_id=current_user.id
    ).first_or_404()

    return send_from_directory(
        current_app.config["UPLOAD_FOLDER"],
        document.file_path,
        as_attachment=True
    )