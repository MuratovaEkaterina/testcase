import csv
import json
from flask import jsonify, request
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
        d = Data(file_id=new_file.id, data=s, line_number=i)
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


@app.route('/file/<int:id>/data', methods=['GET'])
def data(id):
    limit = int(request.args.get('limit'))
    offset = int(request.args.get('offset'))
    data = (
        Data.query.filter(Data.file_id == id).order_by(Data.line_number).
        offset(offset).limit(limit)
    )
    res = []
    for d in data:
        res.append(json.loads(d.data))
    return res


@app.route('/filter', methods=['GET'])
def get_datas():
    datas = Data.query
    for k, v in request.args.items():
        datas = datas.filter(
            Data.data.op("->>")(k).cast(db.String) == v
        )
    datas = datas.all()
    return jsonify([x.data for x in datas])
