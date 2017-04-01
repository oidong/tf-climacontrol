# tf-climacontrol
This project is using virtualenv
1. Start Virtualenv
	source wfdb-venv/bin/activate
2. Start Webserver
	python3 manage.py runserver

Alternative you can start a python shell for testing purposes
	python3 manage.py shell

Start celery server
	celery -A celery_runner worker --loglevel=info
with periodic Tasks
	celery -B -A celery_runner worker --loglevel=info
