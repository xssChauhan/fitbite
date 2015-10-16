from . import db


class Products(db.Model):
	__tablename__ = 'products'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), nullable= False)
	price = db.Column(db.Integer, nullable = False)
	#orders = db.relationship('Orders', backref='product',lazy = 'dynamic')
	images = db.relationship('Images', backref = 'products', lazy = 'dynamic')
	category = db.Column(db.String(25),nullable = True)
	calories = db.Column(db.String(25), nullable = False)
	vegOrNonVeg = db.Column(db.String(10))
	timeToCook = db.Column(db.Integer)
	def __repr__(self):
		return '<Product %r>' % self.name

	@property
	def serialize(self):
		'''Return data in easily serialize format'''
		return{
		'id' 	: self.id,
		'name'	: self.name,
		'images': self.oneToMany,
		'price' : self.price,
		'category' : self.category,
		'calories' : self.calories,
		'vegOrNonVeg' : self.vegOrNonVeg,
		'timeToCook' : self.timeToCook
		}
	@property
	def oneToMany(self):
		return [item.serialize for item in self.images]

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
	productID = db.Column(db.Integer, db.ForeignKey('products.id'))

	def __repr__(self):
		return '<Image %r>'%(self.imageFile)
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

