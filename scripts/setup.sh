pathadd(){
  if [ -d "$1" ] && [[ ":$PATH:" != *":$1:"* ]]; then
    echo 'yas'
    PATH="${PATH:+"$PATH:"}$1"
  fi
}

shenanigans(){
    echo "from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
	app.run(debug=True)" > run.py
    echo Why are we here? Just to suffer?
}

pathadd ~/Library/Python/3.7/bin/
export PATH
pip3 install  --user virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
shenanigans
deactivate
