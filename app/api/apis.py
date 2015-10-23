import os, random
from flask import request,jsonify,send_from_directory, make_response, Response, json
from .. import db
from ..models import Products, Images, Sessions
from . import api
clientID = 45678
imageDIR = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))),'images')

errorMessages = {
	'sessionNotFound'  	: 'Forbidden Use; Cannot identify Session',
	'appIDNotFound': 'Forbidden Use; Cannot Authenticate'
	}

@api.route('/')
def yes():
	return 'Hello'


def findSession(id):
	'''Enhance the robustness by considering in the '''
	s = Sessions.query.filter_by(sID = str(id)).first();
	if s.sID == id:
		return s.activeState
	else:
		raise AuthenticationFailed(errorMessages['sessionNotFound'], status_code = 403)

def deleteSession(id):
	s = Sessions.query.filter_by(sID = str(id)).first()
	if s == []:
		raise AuthenticationFailed(errorMessages['sessionNotFound'])
	else:
		db.session.delete(s)
		db.session.commit()


@api.route('/api/startSession/<int:appID>')
def startSession(appID):
	if appID == clientID:
		hash = random.getrandbits(128)
		s = Sessions(sID = str(hash), activeState = True)
		db.session.add(s)
		db.session.commit()
		return jsonify(json_list = [hash])
	else:
		raise AuthenticationFailed( errorMessages['appIDNotFound'] , status_code = 403)

@api.route('/api/endSession/<sessionID>')
def endSession(sessionID):
	deleteSession(sessionID)
	return 'Session Deleted'

#APIs for getting products
@api.route('/api/get/products/')
def getProducts():
	'''Returns the all the Products List as a HTTP json object'''
	products = Products.query.all()
	a = [e.serialize for e in products]
	return Response(json.dumps(a,indent = 1), mimetype = 'application/json')
	

@api.route('/api/get/product/', methods =['POST'])
def getProductByID():
	'''Returns the Product with the ID as a HTTP json object'''
	id = request.form['id']
	product = Products.query.filter_by(id=id).first()
	if not product:
		abort(404)
	else:
		return jsonify(product.serialize)

@api.route('/api/get/productImage/', methods= ['POST'])
def getProductImage():
	filename = request.form['filename']
	if filename is not None:
	    if filename in os.listdir(imageDIR):
	    	return send_from_directory(imageDIR,filename)
	else:
		return '404 not found'


