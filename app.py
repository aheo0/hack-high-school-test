from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

def dump_json(file, data, json_format=True, json_type=True):
	'''file, data, json=True -> dumps data into a file'''
	filename = file
	if json_format:
		filename = 'json/' + file
	if json_type:
		filename += '.json'

	with open(filename, 'w') as f:
		json.dump(data, f)

with open('json/user_content.json', 'r') as f:
	person = json.load(f)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/hello', methods=['GET'])
def say_hello():
    return jsonify('Hello!', 200)

# If you wanna get a payload, look into that flask.request method above
@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def username_post_put_delete():
	with open('json/user_content.json', 'r') as f:
		person = json.load(f)

	person_request = request.json
	with open('json/random.txt', 'r+') as f:
		json.dump(person_request, f)
	if True:
	#try:
		'''username = request.args.get('username')
		comment = request.args.get('comment')

		#if key has not been inputed correctly
		if username is None and comment is None:
			if request.method == 'GET':
				all = ()
				for i in person:
					all += (i[username] + ': ' + i[comment],)

				if all == ():
					all = 'empty'

				return jsonify(all, 200)

			else:
				return jsonify('Use the GET method to view all the users.', 400)

		if username is None or comment is None:
			return jsonify('Hello World!', 'Incorrect key.', 404)'''

		if request.method == 'GET':
			return jsonify({"user-data":person, "HTTP-error":200})

		elif request.method == 'POST':
			person_request = request.json
			with open('json/random.txt', 'r+') as f:
				f.write(str(person_request))
			user_in_person = None

			if 'username' in person_request and 'comment' in person_request:
				username = person_request['username']
				comment = person_request['comment']
			else:
				return 'You\'re annoying.'

			if username in person:
				return jsonify('Data for this user already exists.', username + ': ' + person[username], 'Please use the PUT method to make changes.', 400)
			else:
				person[username] = comment
				dump_json('user_content', person)
				
				return jsonify({"user-data":person, "HTTP-error":200})

		elif request.method == 'PUT':
			person_request = request.json
			with open('json/random.txt', 'r+') as f:
				f.write(str(person_request))
			user_in_person = None

			if 'username' in person_request and 'comment' in person_request:
				username = person_request['username']
				comment = person_request['comment']
			else:
				return 'You\'re annoying.'

			if username in person:
				person[username] = comment
				dump_json('user_content', person)
				
				return jsonify({"user-data":person, "HTTP-error":200})
			else:
				return jsonify({"user-data": "Data for this user does not exists. Please use the POST method to add new users.", "HTTP-error": 400})

		elif request.method == 'DELETE':
			delete_person = request.json
			delete_user = delete_person['username']

			if delete_user in person:
				del person[delete_user]
				dump_json('user_content', person)
				return jsonify({"message":"User has successfully been deleted from the database.", "HTTP-error": 200})
			else:
				return jsonify(username + ' does not exist in the database.', 400)

	'''
		elif request.method == 'DELETE':
			for i in person:
				if i['username'] == username:
					del person[person.index(i)]
					return jsonify(username + ' has been successfully deleted from the database.', 200)
			return jsonify(username + ' does not exist in the database.', 400)'''

	#except:
		
		#return 'hi'
		#return jsonify('Server has encountered an error.', 500)

	if request.method == 'GET':
		return jsonify('Server has encountered an error.', 400)
	else:
		print(request.method)
		return jsonify('Server has encountered an error', 500)

@app.route('/user/<user>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def username_get(user):
	with open('json/user_content.json', 'r') as f:
		person = json.load(f)

	if request.method == 'GET':
		if user in person:
			return jsonify({"user-data":person[user], "HTTP-error":200})
		else:
			return jsonify('No user found.', 404)
	else:
		return jsonify({"error-message": "Please use the GET method to see this user's data.", "HTTP-error":500})

# If you wanna get a payload, look into that flask.request method above
@app.route('/api/v1/user', methods=['GET', 'POST'])
def api_username_post_put_delete():
	with open('json/user_content.json', 'r') as f:
		person = json.load(f)

	person_request = request.json
	with open('json/random.txt', 'r+') as f:
		json.dump(person_request, f)

	if request.method == 'GET':
		return jsonify({"user-data":person, "HTTP-error":200})

	elif request.method == 'POST':
		person_request = request.json
		with open('json/random.txt', 'r+') as f:
			f.write(str(person_request))
		user_in_person = None

		if 'username' in person_request and 'comment' in person_request:
			username = person_request['username']
			comment = person_request['comment']
		else:
			return 'You\'re annoying.'

		if username in person:
			return jsonify('Data for this user already exists.', username + ': ' + person[username], 'Please use the PUT method to make changes.', 400)
		else:
			person[username] = comment
			dump_json('user_content', person)
			
			return jsonify({"user-data":person, "HTTP-error":200})

	else:
		return jsonify({"error-message":"Wrong method has been used.", "HTTP-error": 400})

@app.route('/api/v1/user/<user>', methods=['GET', 'PUT', 'DELETE'])
def api_specific_user(user):
	with open('json/user_content.json', 'r') as f:
		person = json.load(f)
	person_request = request.json

	if user not in person:
		return jsonify({"error-message":"User does not exist in the database. Please use the POST method to create new ones.", "HTTP-error": 400})

	if request.method == 'GET':
		return jsonify({"user-comment":person[user], "HTTP-error":200})

	elif request.method == 'PUT':
		person_request = request.json
		with open('json/random.txt', 'r+') as f:
			f.write(str(person_request))
		user_in_person = None

		if 'comment' in person_request:
			comment = person_request['comment']
		else:
			return 'You\'re annoying.'

		if user in person:
			person[user] = comment
			dump_json('user_content', person)
			
			return jsonify({"user-data":"New comment: %s" % comment, "HTTP-error":200})
		else:
			return jsonify({"user-data": "Data for this user does not exists. Please use the POST method to add new users.", "HTTP-error": 400})

	elif request.method == 'DELETE':
		if user in person:
			del person[user]
			dump_json('user_content', person)
			return jsonify({"message":"User has successfully been deleted from the database.", "HTTP-error": 200})
		else:
			return jsonify(username + ' does not exist in the database.', 400)

	else:
		return jsonify({"error-message":"Wrong method has been used.", "HTTP-error": 400})


@app.route('/goodbye', methods=['GET'])
def say_goodbye():
    return 'Goodbye!'


if __name__ == '__main__':
    app.run(debug=True)
