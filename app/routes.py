import csv
from flask import request
from app import app, db
from io import TextIOWrapper
from .models import File, Data


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    f = TextIOWrapper(file)
    reader = csv.DictReader(f)
    fields = ', '.join(reader.fieldnames)
    new_file = File(name=file.filename, fields=fields)
    db.session.add(new_file)
    db.session.commit()
    for i, s in enumerate(reader):
        d = Data(file_id=new_file.id, data=str(s), line_number=i)
        db.session.add(d)
        db.session.commit()
    return {'success': True}


@app.route('/files', methods=['GET'])
def files():
    files = File.query.all()
    res = []
    for file in files:
        res.append({'id': file.id, 'name': file.name})
    return res


@app.route('/file/<int:id>', methods=['GET'])
def show_fields(id):
    file = File.query.get(id)
    return {'name': file.name, 'fields': file.fields}
