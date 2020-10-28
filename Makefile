.PHONY: test

init:
	pip install -r requirements.txt

test:
	pytest

build:
	python setup.py sdist bdist_wheel

clean:
	rm -fr build istacpy.egg-info dist
