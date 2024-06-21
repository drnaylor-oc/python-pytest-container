#!/bin/bash

# install poetry
curl -sSL https://install.python-poetry.org | python3 -

# ensure we have pytest
pip install pytest