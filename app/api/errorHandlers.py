from . import api
class AuthenticationFailed(Exception):
	status_code = 403
	def __init__(self, message,status_code = None,payload = None):
		Exception.__init__(self)
		self.message = message
		if self.status_code is not None:
			self.status_code = status_code
		self.payload = payload

	def to_dict(self):
		rv = dict(self.payload or ())
		rv['message'] = self.message
		return rv

class NotFound(Exception):
	status_code = 404
	message = "Oops. This is barren land. Ain't nowhere to go from here!"
	def __init__(self, message = None, status_code = None, payload = None):
		Exception.__init__(self)
		if message is not None:
			self.message = message
		if status_code is not None:
			self.status_code = status_code
		self.payload = payload

	def to_dict(self):
		rv = dict(self.payload or ())
		rv['message'] = self.message
		return rv


@api.errorhandler(AuthenticationFailed)
def authentication_failed(error):
	response = jsonify(error.to_dict())
	response.status_code = error.status_code
	return response

@api.errorhandler(NotFound)
def notFound(error):
	response = jsonifgy(error.to_dict())
	response.status_code = error.status_code
	return response

@api.errorhandler(Exception)
def errors(error):
	return 'From API Blueprint: ' + repr(error)

@api.errorhandler(404)
def notFound(error):
	return error
