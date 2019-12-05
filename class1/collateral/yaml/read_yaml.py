#!/usr/bin/env python
import yaml
from pprint import pprint


def read_yaml(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


def write_yaml(filename, output, style=None):
    with open(filename, "wt") as f:
        if style == "compressed":
            yaml.dump(output, f, default_flow_style=True)
        else:
            yaml.dump(output, f, default_flow_style=False)


if __name__ == "__main__":
    file_name = input("Enter your YAML filename: ")
    yaml_out = read_yaml(file_name)
    pprint(yaml_out)

    # import json
    # print(json.dumps(yaml_out))
