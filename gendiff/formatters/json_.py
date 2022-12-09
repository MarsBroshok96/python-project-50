import json


def format(tree: list):
    """
    Convert tree with diffs to string in json format.
    """
    result = json.dumps(tree, indent=4)
    return result
