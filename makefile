PYTHON = python3 manage.py


run:
	${PYTHON} runserver

migrate:
	${PYTHON} makemigrations
	${PYTHON} migrate
