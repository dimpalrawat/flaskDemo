from appConnection import app
from appConnection import db
from User import User
from flask import jsonify


@app.route('/get')
def getAll():
	users = User.query.all()
	print(type(users))
	return "Users printed on console"


@app.route('/save/<username>/<email>')
def save(username, email):
	user = User(username=username, email=email)
	db.session.add(user)
	db.session.commit()
	return "User saved!!"


@app.route('/getByUsername/<username>')
def getByUsername(username):
	user = User.query.filter_by(username=username).first()
	try:
		userHandling(user)
	except:
		return "No valid user found for this query"
	return "Found user with username: " + user.username + " email: " + user.email


@app.route('/getByEmail/<email>')
def getByEmail(email):
	user = User.query.filter_by(email=email).first()
	try:
		userHandling(user)
	except:
		return "No valid user found for this query"
	return "Found user with username: " + user.username + " email: " + user.email


def userHandling(user):
	if user is None:
		raise Exception("No valid user found for this query")
	print("Valid user found: " + str(user))
	return


if __name__ == '__main__':
	app.run(host='0.0.0.0')