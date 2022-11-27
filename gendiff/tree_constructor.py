"""
Module that contain constructor and selectors of 1lvl mutable tree abstraction
"""


def construct_1lvl_mutable_tree(file: dict, common_meta=
        {
            'diff_status': "   ", 'origin': 1
            }
        ):
    """
    Construct tree whrere each node/leaf is list with content in the following order: 0 - node_name, 1 - node_value, 2 - node meta
    """
    tree = []

    for tuple in file.items():
        key, val = tuple
        tree.append([key, val, common_meta])
    return tree


def get_node(tree, node_name, origin=1):
    for node in tree:
        if node[0] == node_name and node[2]['origin'] == origin:
            return node
    raise Exception(f'Nothing there with name - "{node_name}" and origin - "{origin}"')


def get_value(node: list):
    return node[1]


def get_name(node: list):
    return node[0]


def get_meta(node: list):
    return node[2]
