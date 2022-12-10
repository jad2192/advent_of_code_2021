lint:
	poetry run flake8 --extend-ignore E203 --max-line-length 120 .
	poetry run mypy .
	poetry run isort -c .
	poetry run black -l 120 --check --diff .

fmt:
	poetry run isort .
	poetry run black -l 120 .

test:
	poetry run pytest .