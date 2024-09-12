
install:
	pip install --upgrade pip && pip install -r Requirements.txt

format:
	black *.py

lint:
	pylint --ignore-patterns=test_.*?py *.py
	
test: 
	python -m pytest -cov=main test_main.py

all: install format lint test 