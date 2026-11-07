import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, send_from_directory
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from extensions import db
from models.document import Document

documents_bp = Blueprint("documents", __name__)

ALLOWED_EXTENSIONS = {"pdf", "doc", "docx", "txt", "png", "jpg", "jpeg"}


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

        if "." not in filename or filename.rsplit(".", 1)[1].lower() not in ALLOWED_EXTENSIONS:
            flash("File type not allowed")
            return redirect(url_for("documents.upload"))

        upload_folder = current_app.config["UPLOAD_FOLDER"]
        os.makedirs(upload_folder, exist_ok=True)

        file.save(os.path.join(upload_folder, filename))

        document = Document(
            filename=filename,
            file_path=filename,
            owner_id=current_user.id
        )

        db.session.add(document)
        db.session.commit()

        flash("File uploaded successfully!")

    return render_template("upload.html")


# View Documents
@documents_bp.route("/documents")
@login_required
def view_documents():

    documents = Document.query.filter_by(
        owner_id=current_user.id
    ).all()

    return render_template("documents.html", documents=documents)


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