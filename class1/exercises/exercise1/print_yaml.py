#!/usr/bin/env python
import sys
import yaml


def read_yaml(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError as e:
        raise e("You need to specify the file you wish to print!")
    print(read_yaml(filename))
