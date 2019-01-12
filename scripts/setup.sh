pathadd(){
  if [ -d "$1" ] && [[ ":$PATH:" != *":$1:"* ]]; then
    echo 'yas'
    PATH="${PATH:+"$PATH:"}$1"
  fi
}
pathadd ~/Library/Python/3.7/bin/
export PATH
pip3 install  --user virtualenv
virtualenv ../venv
source ../venv/bin/activate
pip3 install -r requirements.txt
deactivate
