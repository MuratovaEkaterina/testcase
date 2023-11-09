from app import db, app
from sqlalchemy.dialects.postgresql import JSON


class File(db.Model):
    __tablename__ = 'file'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    fields = db.Column(db.String(1000))

    pr = db.relationship('Data', backref='file', uselist=False)


class Data(db.Model):
    __tablename__ = 'data'

    file_id = db.Column(db.Integer, db.ForeignKey('file.id'))
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSON)
    # data = db.Column(db.String(1000))
    line_number = db.Column(db.Integer)
