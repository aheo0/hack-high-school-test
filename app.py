from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

person = [
	{'username': 'admin',	'comment': 'admin\'s comment'},
	{'username': 'bob',		'comment': 'bob\'s comment'},
	{'username': 'carl',	'comment': 'carl\'s comment'}
]


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/hello', methods=['GET'])
def say_hello():
    return jsonify('Hello!', 200)

@app.route('/user/<user>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def username_get(user):
	if request.method == 'GET':
		user_in_person = None
		for i in person:
			if i['username'] == user:
				user_in_person = person.index(i)
		
		if user_in_person is not None:
			person_data = person[user_in_person]
			return jsonify(user + ': ' + person_data['comment'])
		return jsonify('No user found.')

@app.route('/user', methods=['POST', 'PUT', 'DELETE'])
def username_post_put_delete():
	username = request.args.get('username')
	comment = request.args.get('comment')

	#if key has not been inputed correctly
	if username is None or comment is None:
		return jsonify('Hello World!')

	if request.method == 'POST':
		user_in_person = None
		for i in person:
			if i['username'] == username:
				user_in_person = person.index(i)
		
		if user_in_person is not None:
			person_data = person[user_in_person]
			return jsonify('Data for this user already exists.\n' + username + ': ' + person_data['comment'] + '\nPlease use the PUT method to make changes.')

		else:
			new_user = {'username': username, 'comment': comment}
			person.append(new_user)
			return jsonify(username + ': ' + comment)

	elif request.method == 'PUT':
		user_in_person = None
		for i in person:
			if i['username'] == username:
				user_in_person = person.index(i)
		
		if user_in_person is None:
			return jsonify('Data for this user does not exists.\nPlease use the POST method to add new users.')

		else:
			person_data = person[user_in_person]
			del person[user_in_person]
			person_data['comment'] = comment
			person.append(person_data)
			return jsonify(username + ': ' + comment)

	elif request.method == 'DELETE':
		for i in person:
			if i['username'] == username:
				del person[person.index(i)]
				return jsonify(username + ' has been successfully deleted from the database.')
		return jsonify(username + ' does not exist in the database.')

@app.route('/goodbye', methods=['GET'])
def say_goodbye():
    return 'Goodbye!'


if __name__ == '__main__':
    app.run(debug=True)
