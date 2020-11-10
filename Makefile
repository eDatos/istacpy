.PHONY: test

init:
	pip install -r requirements.txt

test:
	pytest

build:
	python setup.py sdist bdist_wheel

clean:
	rm -fr build istacpy.egg-info dist
	rm -fr .coverage htmlcov/

coverage:
	coverage run -m pytest
	coverage html
	open htmlcov/index.html

test-publish:
	twine upload --repository testpypi dist/*

publish:
	twine upload dist/*
