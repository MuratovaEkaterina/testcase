from app import db


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    fields = db.Column(db.String(1000))


class Data(db.Model):
    file_id = db.Column(db.Integer, db.ForeignKey('file.id'))
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    line_number = db.Column(db.Integer)
