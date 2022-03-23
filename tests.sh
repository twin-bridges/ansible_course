#!/bin/bash

# source ./env_vars

pylama .
black --check .
cd tests
py.test -s -v test_class*
py.test -s -v test_bonus*
