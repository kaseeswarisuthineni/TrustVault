from extensions import db


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(db.String(255), nullable=False)

    file_path = db.Column(db.String(500), nullable=False)

    owner_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    uploaded_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    owner = db.relationship("User", backref="documents")