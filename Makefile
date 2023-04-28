MANAGE := poetry run python3 manage.py

start:
	${MANAGE} runserver 127.0.0.1:8000
shell:
	${MANAGE} shell_plus --plain
db:
	${MANAGE} dbshell
migrate:
	${MANAGE} makemigrations
	${MANAGE} migrate
collectstatic:
	${MANAGE} collectstatic --no-input --clear
test:
	${MANAGE} test --keepdb
install:
	poetry install --no-root
lint:
	poetry run flake8 graphql_django --exclude migrations