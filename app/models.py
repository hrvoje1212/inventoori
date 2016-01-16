from app import db, app
from hashlib import md5

import flask.ext.whooshalchemy as whooshalchemy


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	items = db.relationship('Item', backref='holder', lazy='dynamic')

	def avatar(self, size):
		return 'http://www.gravatar.com/avatar/{}?d=mm&s={}'.format(
			md5(self.email.encode('utf-8')).hexdigest(), size)

	def __repr__(self):
		return self.username


class Item(db.Model):
	__searchable__ = ['name', 'location', 'serial_number', 'description']

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250))
	location = db.Column(db.String(250))
	serial_number = db.Column(db.String(250))
	description = db.Column(db.String(250))
	holder_id = db.Column(db.Integer, db.ForeignKey('user.id'))

whooshalchemy.whoosh_index(app, Item)