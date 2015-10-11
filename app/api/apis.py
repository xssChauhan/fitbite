import os
from flask import jsonify
from .. import db
from ..models import Products, Images
from . import api
from .errorHandlers import AuthenticationFailed


@api.errorhandler(AuthenticationFailed)
def authentication_failed(error):
	response = jsonify(error.to_dict())
	response.status_code = error.status_code
	return response

@api.errorhandler(Exception)
def errors(error):
	return 'From API Blueprint: ' + repr(error)

@api.errorhandler(404)
def notFound():
	pass


#APIs for getting products
@api.route('/api/<auth>/get/products/')
def getProducts(auth):
	'''Returns the all the Products List as a HTTP json object'''
	if auth is not None:
		products = Products.query.all()
		return jsonify(json_list = [e.serialize for e in products])
	else:
		raise AuthenticationFailed('Forbidden Use; Authentication Failed', status_code = 403)

@api.route('/api/<auth>/get/product/<int:id>')
def getProductByID(auth,id):
	'''Returns the Product with the ID as a HTTP json object'''
	if auth is not None:
		product = Products.query.filter_by(id=id).first()
		return jsonify(product.serialize)
	else:
		raise AuthenticationFailed('Forbidden Use; Authentication Failed', status_code = 403)

@api.route('/api/get/productImage/<filename>')
def getProductImage(filename):
	pass
	
