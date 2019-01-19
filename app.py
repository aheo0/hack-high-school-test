from flask import Flask, request, jsonify, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/hello', methods=['GET'])
def say_hello():
    return jsonify('Hello!', 200)


@app.route('/goodbye', methods=['GET'])
def say_goodbye():
    return 'Goodbye!'


if __name__ == '__main__':
    app.run(debug=True)
