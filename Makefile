files = ls wsgi_wovn/*.py tests/*.py example/*.py

pep8:
	$(files) | xargs pep8

autopep8:
	$(files) | xargs autopep8 -i
