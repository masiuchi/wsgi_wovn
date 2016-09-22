pep8:
	ls wsgi_wovn/*.py tests/*.py | xargs pep8

autopep8:
	ls wsgi_wovn/*.py tests/*.py | xargs autopep8 -i
