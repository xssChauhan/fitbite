from . import db


class Products(db.Model):
	__tablename__ = 'products'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), nullable= False)
	images = db.Column(db.String(100), nullable = True)
	price = db.Column(db.Integer, nullable = False)
	#orders = db.relationship('Orders', backref='product',lazy = 'dynamic')
	#images = db.relationship('Images', backref = 'product', lazy = 'dynamic')
	def __repr__(self):
		return '<Product %r>' % self.name

	@property
	def serialize(self):
		'''Return data in easily serialize format'''
		return{
		'id' 	: self.id,
		'name'	: self.name,
		'images': self.images,
		'price' : self.price
		}

class Orders(db.Model):
	__tablename__ = 'orders'
	id = db.Column(db.Integer, primary_key = True)
	orderID = db.Column(db.Integer, primary_key = True)

	def __repr__(self):
		return '<Order %r>' % self.orderID

	@property
	def serialize(self):
		return{
		'id'	  :self.id,
		'orderID' : self.orderID
		}


class Images(db.Model):
	__tablename__ = 'images'
	id = db.Column(db.Integer, primary_key = True)
	imageFile = db.Column(db.String(100), nullable = False)
	imageSize = db.Column(db.String(10), nullable = False)
	#productID = db.Column(db.Integer, db.ForeignKey('product.id'))

	def __repr__(self):
		return '<Image %r>'%(self.imageFile, self.productID)
	@property
	def serialize(self):
		return{
		'id'		: self.id,
		'imageFile' : self.imageFile,
		'imageSize' : self.imageSize,
		'productID' : self.productID
		}

class Sessions(db.Model):
	__tablename__ = 'sessions'
	sID = db.Column(db.String(50), primary_key = True, nullable = False)
	activeState = db.Column(db.Boolean,nullable = False, default = False)

	def __repr__(self):
		return '<Session %r>' %(self.sID)