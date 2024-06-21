# Skeleton Pytest project

This project is desgined to show how we can use Pytest in an src/test directory format.

## Requirements

* Tested against Python 3.12, though older versions should work
* pytest 7+

If you are using Visual Studio Code and have the Dev Containers extension installed, you can run this within a dev container which will resolve dependencies for you.

You can also install the [Poetry build tool](https://python-poetry.org/) if you wish, `pyproject.toml` contains directives to install pytest.

## Writing Tests

Files containing tests must names that are prefixed by `test_` or suffixed by `_test`, and of type `.py`. See the `sample_test.py` file for a couple of sample tests.

## Running Tests

In your terminal, from the `project` directory, run `pytest`, or if using poetry, `poetry run pytest`.
