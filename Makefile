test: lint test-python

lint:
	@echo ""

db:
	@echo "Creating database"
	python initdb.py

test-python:
	@echo "Running tests"
	python run_test.py

server:
	python server.py

server-prod:
	gunicorn --bind 0.0.0.0:8000 src.app:application -e deploy=dev

docker-start:
	docker-compose up -d db
	docker-compose run --rm webapp /bin/bash -c "cd /code/src && python initdb.py"
	docker-compose up -d

docker-stop:
	docker-compose stop db
	docker-compose stop webapp
	docker-compose stop nginx
