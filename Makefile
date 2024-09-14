
install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py
	
test: 
	python -m pytest -cov=main test_main.py

lint:
	pylint --disable=R,C,locally-disabled --ignore-patterns=test_.*?py *.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy

generate_and_push:
	# Create the markdown file (assuming it's generated from the plot)
	python test_main.py  # Replace with the actual command to generate the markdown

	# Add, commit, and push the generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add chart.png stocks.md; \
		git commit -m "Add generated plot and report"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi 