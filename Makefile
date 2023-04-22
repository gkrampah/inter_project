CHANNELS := conda-forge bioconda
install:
	conda install -y --file requirements.txt $(foreach channel,$(CHANNELS),-c $(channel))

format:
	black *.py

lint:
	pylint --disable=R,C dummy_script.py #update to this download script

test:
	python -m pytest -vv test_dummy_script.py

all: 
	install format lint test
