init:
	pip install -r requirements.txt

test:
	nosetests tests

build:
	python setup.py sdist bdist_wheel

clean:
	rm -fr build istacpy.egg-info dist
