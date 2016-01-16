from flask import (
	render_template, flash, redirect, session, url_for, request,
	jsonify
)
from app import app, db
from app.models import User, Item
from app.forms import CreateUserForm, CreateItemForm
from sqlalchemy.exc import IntegrityError

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
	user = { "nickname": 'Hrvoje'}

	users = User.query.all()
	items = []

	return render_template('index.html', title='Home', user=user,
		users=users, items=items
	)


@app.route('/user/<username>')
def user(username):
	user = User.query.filter_by(username=username).first()

	if user == None:
		flash('User %s not found.' % username)
		return redirect('index')

	return render_template('user_profile.html', user=user, title='Profile')


@app.route('/users')
def users_list():
	users = User.query.all()

	return render_template('users_list.html', users=users, title='Users')


@app.route('/user/create', methods=['GET', 'POST'])
def create_user():
	form = CreateUserForm()

	if form.validate_on_submit():
		username = form.username.data
		email = form.email.data

		user = User(username=username, email=email)
		db.session.add(user)
		db.session.commit()

		flash('New user created with username="%s", email=%s' %
              (form.username.data, str(form.email.data)))

		return redirect('/index')

	return render_template('user.html', action='Create',
		data_type='new user', form=form
	)
	return render_template('user.html', form=form, title='Create User')


@app.route('/user/edit/<id>', methods=['GET', 'POST'])
def edit_user(id):
	user = User.query.filter_by(id=id).first()

	if user == None:
		return redirect('create_user')

	form = CreateUserForm(obj=user)

	if form.validate_on_submit():
		username = form.username.data
		email = form.email.data

		user.username = username
		user.email = email

		db.session.commit()

		# flash('Added new item to user %s' % (holder.username))
		return redirect(url_for('edit_user', id=user.id))


	return render_template('user.html', action='Edit',
		data_type=user.id, form=form, title='Edit User'
	)



@app.route('/user/remove/<id>')
def remove_user(id):
	User.query.filter_by(id=id).delete()
	db.session.commit()
	return redirect('index')


@app.route('/item/create', methods=['GET', 'POST'])
def create_item():
	form = CreateItemForm()

	if form.validate_on_submit():
		holder = form.holder.data
		name = form.name.data
		location = form.location.data
		serial_number = form.serial_number.data
		description = form.description.data

		item = Item(
			name=name, location=location, serial_number=serial_number,
			description=description
		)

		if holder:
			holder.items.append(item)

		db.session.commit()

		flash('Added new item to user %s' % (holder.username))

		return redirect('/index')

	return render_template('item.html', action='Create',
		data_type='new item', form=form, title='Create Item'
	)


@app.route('/item/<id>', methods=['GET', 'POST'])
def edit_item(id):
	item = Item.query.filter_by(id=id).first()

	if item == None:
		return redirect('create_item')

	form = CreateItemForm(obj=item)

	if form.validate_on_submit():
		holder = form.holder.data
		name = form.name.data
		location = form.location.data
		serial_number = form.serial_number.data
		description = form.description.data

		item.name = name
		item.location = location
		item.serial_number = serial_number
		item.description = description

		if holder:
			holder.items.append(item)

		db.session.commit()

		# flash('Added new item to user %s' % (holder.username))

		return redirect(url_for('edit_item', id=item.id))


	return render_template('item.html', action='Edit',
		data_type="{}".format(item.id), form=form, title='Edit Item'
	)


@app.route('/item/search/<input>', methods=['GET', 'POST'])
def search_item(input):
	items = Item.query.whoosh_search(str(input)).all()

	return render_template('items_list.html', items=items)


@app.route('/item/remove/<id>')
def remove_item(id):
	Item.query.filter_by(id=id).delete()
	db.session.commit()
	return redirect('index')

