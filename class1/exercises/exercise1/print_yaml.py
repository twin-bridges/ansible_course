#!/usr/bin/env python
import sys
import yaml
from pprint import pprint


def read_yaml(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        filename = input("Enter YAML file name: ")
    pprint(read_yaml(filename))
