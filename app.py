from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash
import json
from functools import wraps

app = Flask(__name__)

app.secret_key = 'M9M6Fv-lj!A-YOSy2T!$je4pJxb&eV9QiFufuC4P3lR'

# login required
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'identification' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


def login_identification(username, password):
    with open('json/users.json') as f:
        users = json.load(f)
        
    if username in users and users[username] == password:
        session['identification'] = {}
        session['identification']['username'] = username
        return True

@app.route('/')
@login_required
def home():
    print(session)
    return 'Hello, World!'

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html', data=session['identification'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    code = None
    try:
        code = request.args.get('code')
        session.pop('identification', None)
    except:
        pass

    error = None

    if request.method == 'GET':
        if 'identification' in session:
            return redirect(url_for('welcome'))

    elif request.method == 'POST':
        if login_identification(request.form['username'], request.form['password']):
            return redirect(url_for('welcome'))
        else:
            error = True

    return render_template('login.html', error=error, code=code)

@app.route('/logout')
def logout():
    session.pop('identification', None)

    return redirect(url_for('welcome'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None

    if request.method == 'GET':
        return render_template('signup.html', error=None)

    elif request.method == 'POST':
        with open('json/users.json') as f:
            users = json.load(f)
        
        # Username taken
        if request.form['username'] in users:
            return render_template('signup.html', error="username")

        # Add username
        users[request.form['username']] = request.form['password']

        with open('json/users.json', 'r+') as f:
            f.truncate()
            json.dump(users, f)
        
        # Now log in
        return redirect('login?code=1')


if __name__ == '__main__':
	app.run(debug=True)