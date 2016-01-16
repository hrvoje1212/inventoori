from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

from app.models import User

class CreateUserForm(Form):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])

def get_all_users():
	return User.query.all()

class CreateItemForm(Form):
	name = StringField('name', validators=[DataRequired()])
	location = StringField('location', validators=[DataRequired()])
	serial_number = StringField('serial_number', validators=[DataRequired()])
	description = StringField('description', widget=TextArea(),
		validators=[DataRequired()]
	)
	holder = QuerySelectField(
		query_factory=get_all_users,
		allow_blank=True
	)
