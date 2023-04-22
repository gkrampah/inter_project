CHANNELS := conda-forge bioconda
install:
	conda install -y --file requirements.txt $(foreach channel,$(CHANNELS),-c $(channel))

format:
	black *.py

lint:
	pylint --disable=R,C download_script.py

test:
	python -m pytest -vv test_dummy_script.py

all: 
	install format lint test
