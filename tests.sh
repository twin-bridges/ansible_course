#!/bin/bash

# source ./env_vars

pylama .
black --check .
cd tests
pytest -p no:pylama -s -v test_class*
pytest -p no:pylama -s -v test_bonus*
