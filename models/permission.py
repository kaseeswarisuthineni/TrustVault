from extensions import db


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    document_id = db.Column(
        db.Integer,
        db.ForeignKey("document.id"),
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    access_type = db.Column(db.String(20), nullable=False)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    document = db.relationship("Document", backref="permissions")

    user = db.relationship("User", backref="permissions")