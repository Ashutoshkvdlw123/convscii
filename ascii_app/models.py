from ascii_app import db
from datetime import datetime


class TextItem(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    dt = db.Column(db.DateTime(), unique=True, nullable=False, default=datetime.utcnow)
    font = db.Column(db.String(), nullable=False)
    text = db.Column(db.String(), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"TextItem({id}, {text[-1:10]})"
