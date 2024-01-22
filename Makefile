lint:
	poetry run flake8 gendiff

gen-diff:
	poetry run gendiff

build:lint
	poetry build

package-install: # python3 -m pip install --user dist/*.whl
	python3 -m pip install dist/*.whl

check:
	poetry run pytest -v

install:
	pip install poetry
	poetry install

tests-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
