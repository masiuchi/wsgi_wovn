files = find ./ -type f -name "*.py"

test:
	python setup.py test

pep8:
	$(files) | xargs pep8

autopep8:
	$(files) | xargs autopep8 -i

flake8:
	$(files) | xargs flake8

pylint:
	$(files) | xargs pylint
