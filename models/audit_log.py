from extensions import db


class AuditLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=True
    )

    document_id = db.Column(
        db.Integer,
        db.ForeignKey("document.id"),
        nullable=True
    )

    action = db.Column(db.String(100), nullable=False)

    details = db.Column(db.Text)

    timestamp = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    user = db.relationship("User", backref="audit_logs")

    document = db.relationship("Document", backref="audit_logs")