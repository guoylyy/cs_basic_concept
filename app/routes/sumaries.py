from app import app, db
from app.models import sumary
from flask import abort, jsonify, request
import datetime
import json
from flask import render_template

@app.route('/review/sumaries', methods = ['GET'])
def get_all_sumaries():
    entities = sumary.Sumary.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/review/sumaries/<int:id>', methods = ['GET'])
def get_sumary(id):
    entity = sumary.Sumary.query.get(id)
    if not entity:
        abort(404)
    #return jsonify(entity.to_dict())
    return render_template('pages2.html',entity=entity)
    

@app.route('/review/sumaries', methods = ['POST'])
def create_sumary():
    entity = sumary.Sumary(
        summary = request.form['summary']
        , email = request.form['email']
    )
    entity.is_send = False
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict())

@app.route('/review/sumaries/<int:id>', methods = ['PUT'])
def update_sumary(id):
    entity = sumary.Sumary.query.get(id)
    if not entity:
        abort(404)
    entity = sumary.Sumary(
        summary = request.json['summary'],
        email = request.json['email'],
        want_name = request.json['want_name'],
        is_send = request.json['is_send'],
        myattr = request.json['myattr'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200

@app.route('/review/sumaries/<int:id>', methods = ['DELETE'])
def delete_sumary(id):
    entity = sumary.Sumary.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
