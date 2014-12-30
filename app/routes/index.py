from app import app
from app.models import sumary
from flask import abort, jsonify, request, redirect, render_template

@app.route('/', methods = ['GET'])
@app.route('/<int:id>', methods = ['GET'])
def root(id=None):
	try:
		if id:
			entity = sumary.Sumary.query.get(id)
			return render_template('pages2.html',entity=entity)
		else:
			return render_template('pages.html')
	except Exception, e:
		return render_template('pages.html')

