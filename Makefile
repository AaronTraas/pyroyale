# Define required macros here
SHELL = /bin/sh

SRCDIR = ./pyroyale
TESTDIR = ./tests

clean:
	python3 setup.py clean
	rm -rf build dist .pytest_cache *.egg-info $(SRCDIR)/__pycache__ $(TESTDIR)/__pycache__ MANIFEST .scannerwork .openapi-generator/ htmlcov/ .coverage coverage.xml

delete-models:
	rm -rf docs
	rm -rf pyroyale/models

install:
	pip3 install -r requirements.txt
	python3 setup.py install

develop:
	pip3 install -r requirements.txt
	python3 setup.py develop

test-depend:
	pip3 install -r test-requirements.txt
	pip3 install coverage pytest pytest-runner requests_mock

test: test-depend
	python3 setup.py test

integration: develop
	python3 -m pytest -rApP integration

coverage: test-depend
	coverage run setup.py test
	coverage xml

coverage-html: coverage
	coverage html

sonar: coverage
	sonar-scanner -Dsonar.projectVersion=`python -c "import sys; from pyroyale._version import __version__; sys.stdout.write(__version__)"`

upload:
	python3 setup.py sdist bdist_wheel
	twine upload dist/*

swagger: delete-models
	openapi-generator generate -i https://raw.githubusercontent.com/AaronTraas/clashroyale-swagger/master/swagger.yaml -g python -DpackageName=pyroyale -o .
	cat templates/README_suffix.md >> README.md

swagger-local: delete-models
	openapi-generator generate -i ../clashroyale-swagger/swagger.yaml -g python -DpackageName=pyroyale -o .
	cat templates/README_suffix.md >> README.md
