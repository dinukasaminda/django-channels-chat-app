# googlemapImageToTrainTransitWayPoints

##virtualenv -p python3 env

virtualenv -p python3 env
Update after OP's edit:

There was a bug in the OP's version of virtualenv, as described here. The problem was fixed by running:

pip install --upgrade virtualenv
from https://stackoverflow.com/questions/23842713/using-python-3-in-virtualenv

---

source env/bin/activate
pip3 install django
django-admin startproject justchat
mv ./justchat ./src
cd src
python3 manage.py startapp chat
python3 manage.py migrate
python3 manage.py runserver

pip3 install channels

if use docker you need to run docker like this : \$ docker run -p 6379:6379 -d redis:2.8
