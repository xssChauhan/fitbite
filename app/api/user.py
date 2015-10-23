from .. import UserMixin, login_manager,login_required
from .  import api
from flask import Response
class User(UserMixin):
	user_database = {"JohnDoe" : ("John Doe", "John"), 
					"JaneDoe" :("JaneDoe", "Jane")}

	def __init__(self, username, password):
		self.id = username
		self.password = password

	@classmethod
	def get(cls, id):
		return cls.user_database.get(id)


@login_manager.request_loader
def load_user(request):
	token = request.headers.get('Authorisation')
	print request.headers
	if token is None:
		token = request.args.get('token')
	print token
	if token is not None:
		username, password=  token.split(":")
		user_entry = User.get(username)
		if (user_entry is not None):
			user = User(user_entry[0], user_entry[1])
			if (user.password == password):
				return user
	return None

@api.route("/main", methods=["GET"])
def index():
	return Response(response= "Hello World", status= 200)

@api.route('/protected/', methods = ["GET"])
@login_required
def protected():
	return Response(response = "Hello Protected World", status = 200)
