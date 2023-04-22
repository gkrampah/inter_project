install:
	conda install --file requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C script_download.py

test:
	python -m pytest -vv test_dummy_script.py

all: 
	install format lint test
