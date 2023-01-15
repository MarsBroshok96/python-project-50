import json


def format_(tree: list):
    """
    Convert tree with diffs to string in json format.
    """
    result = json.dumps(tree['children'], indent=4)
    return result
