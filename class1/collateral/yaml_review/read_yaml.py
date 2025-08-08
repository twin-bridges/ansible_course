#!/usr/bin/env python
import yaml
from rich import print


def read_yaml(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


if __name__ == "__main__":
    file_name = input("Enter your YAML filename: ")
    yaml_out = read_yaml(file_name)
    print(yaml_out)
