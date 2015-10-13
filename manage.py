import os 
from app import create_app, db
from app.models import Images, Orders, Products, Sessions
from flask.ext.script import Manager

app = create_app()
manager = Manager(app)

if __name__ == '__main__':
	manager.run()