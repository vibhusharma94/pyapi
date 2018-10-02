================================
Setup instructions
================================

Install git:
1. sudo apt-get update
2. sudo apt-get install gi

Install docker:

1. Follow instruction here - https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04

Git pull repo:

1. git clone https://github.com/hellofreshdevtests/vibhusharma94-api-test.git
2. cd vibhusharma94-api-test
3. git fetch && git checkout dev


Start docker container:

1. make docker-start
2. visit http://127.0.0.1:8080/recipe

Stop docker container:

1. make docker-stop



Management commands
---------------------------

Start Dev server:
	make server

Start prod server
	make server-prod

Run test:
   make test

Create database table:
  make initdb

Check test coverage:
	coverage run --source src run_test.py
	coverage report -m


See Makefile for all available commands.


Technology used:

1. Python 3.6
2. Postgres 9.6.5
3. SQLAlchemy ( python orm )
4. Gunicorn ( web server )
5. Git ( version control )
6. Docker ( for containerization )
7. Nginx ( proxy server )
8. PyJWT ( JWT authentication )
9. unittest ( for test cases )


Folder architecture:

1. cmd  - bash scripts for docker setup commands
2. docs - consists documentation and setup instratuctions .rst files
3. tests - test cases goes here
4. src - source code
5. src/web - consist wsgi request and response wrapers
6. src/validators - all kind of data validations modules e,g Request payload validation
7. src/urils - Utility functions. such as pagination, shortcuts etc..
8. src/routers - URL routes definations
9. src/handlers - Http requests handlers modules
10. src/configurations - app settings
11. src/common - common modules to use across the app
12. src/common/constants - defines constants e.g Http status code etc..
13. src/common/exceptions - All kind of exceptions. e.g Http expection ...
14. src/common/mixins - contains modules to use by other modules by class inheritence.




