install:
	conda install --file requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C script_download.py

all: install format lint
