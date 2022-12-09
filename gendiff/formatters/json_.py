import json


def format(tree: list):
    result = json.dumps(tree, indent=4)
    result += '\n'
    return result
