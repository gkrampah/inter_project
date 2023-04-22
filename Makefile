CHANNELS := conda-forge bioconda
install:
	conda install --file requirements.txt $(foreach channel,$(CHANNELS),-c $(channel))
	pip install pylint pytest pytest-cov black

format:
	black *.py

lint:
	pylint --disable=R,C dummy_script.py #update to this download script

test:
	python -m pytest -vv test_dummy_script.py

all: 
	install format lint test
