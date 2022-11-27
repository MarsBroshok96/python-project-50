
install:
	poetry install
gendiff:
	poetry run gendiff
build:
	poetry build
publish: # publish wo add to PyPi
	poetry publish --dry-run
package-install: #install from OS
	python3 -m pip install --force-reintall --user dist/*.whl
lint: #flake8 gendiff dir
	poetry run flake8 gendiff
test-coverage:
	poetry run pytest --cov=gendiff
test:
	poetry run pytest
