from app import app, db
from app.models import mainpage
from flask import abort, jsonify, request
import datetime
import json

@app.route('/api/mainpages', methods = ['GET'])
def get_all_mainpages():
    entities = mainpage.Mainpage.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/api/mainpages/<int:id>', methods = ['GET'])
def get_mainpage(id):
    entity = mainpage.Mainpage.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/api/mainpages', methods = ['POST'])
def create_mainpage():
    entity = mainpage.Mainpage(
        test = request.json['test']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/api/mainpages/<int:id>', methods = ['PUT'])
def update_mainpage(id):
    entity = mainpage.Mainpage.query.get(id)
    if not entity:
        abort(404)
    entity = mainpage.Mainpage(
        test = request.json['test'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200

@app.route('/api/mainpages/<int:id>', methods = ['DELETE'])
def delete_mainpage(id):
    entity = mainpage.Mainpage.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
