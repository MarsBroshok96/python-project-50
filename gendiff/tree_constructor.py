"""
Module that contain constructor and selectors of 1lvl mutable tree abstraction
"""


def gen_diff_dict(old: dict, new: dict):
    """
    Takes two dicts and generate dict with differences in meta:
    {'diff_status':'nested'/'removed'/'added'}
    args:

    old: first dict (before change)
    new: second dict (after change)
    returns:
    diffs with differences and diff status in meta
    """

    diffs = {}
    old_keys = set(old.keys())
    new_keys = set(new.keys())

    added_keys = new_keys - old_keys
    for key in added_keys:
        diffs[key] = {'diff_status': 'added', 'value': new[key]}

    removed_keys = old_keys - new_keys
    for key in removed_keys:
        diffs[key] = {'diff_status': 'removed', 'value': old[key]}

    common_keys = old_keys & new_keys
    for key in common_keys:
        old_value = old[key]
        new_value = new[key]
        if isinstance(old[key], dict) and isinstance(new[key], dict):
            diffs[key] = {'diff_status': 'complex',
                          'value': gen_diff_dict(old_value, new_value)
                          }
        else:
            diffs[key] = {'diff_Status': 'new',
                          'old_value': old_value, 'new_value': new_value
                          }
            if new_value == old_value:
                diffs[key] = {'diff_status': 'old', 'value': old_value}

    return diffs


def make_tree_list(old: dict, new: dict):
    """
    Takes two dicts and generate dict with differences in meta:
    {'diff_status':'nested'/'removed'/'added'}
    args:

    old: first dict (before change)
    new: second dict (after change)
    returns:
    diffs with differences and diff status in meta
    """

    return gen_diff(old, new)


def gen_diff(old, new):

    diffs = []
    old_keys = set(old.keys())
    new_keys = set(new.keys())

    added_keys = new_keys - old_keys
    for key in added_keys:
        diffs.append([key, treat_val(new[key]), {'diff_status': 'added'}])

    removed_keys = old_keys - new_keys
    for key in removed_keys:
        diffs.append([key, treat_val(old[key]), {'diff_status': 'removed'}])

    common_keys = old_keys & new_keys
    for key in common_keys:
        old_value = old[key]
        new_value = new[key]
        if isinstance(old[key], dict) and isinstance(new[key], dict):
            diffs.append([key, gen_diff(old_value, new_value),
                          {'diff_status': ''}
                          ])
        else:
            if new_value == old_value:
                diffs.append([key, treat_val(old_value),
                              {'diff_status': 'old'}
                              ])

            else:
                diffs.append([key, treat_val(new_value),
                              {'diff_status': 'new_value'}
                              ])
                diffs.append([key, treat_val(old_value),
                              {'diff_status': 'old_value'}
                              ])

    return diffs


def treat_val(val, diff_status=''):
    if isinstance(val, dict):
        formated_val = [[k, treat_val(v)] for k, v in val.items()]
        for sub_val in formated_val:
            sub_val.append({'diff_status': diff_status})
        return formated_val
    return val


def format_tree(tree: list):
    for node in tree:
        if isinstance(node, dict) and 'diff_status' not in node:
            formated_node = [[k, v] for k, v in node.items()]
            for sub_node in formated_node:
                sub_node.append({'diff_status': ''})
            tree[tree.index(node)] = formated_node
            format_tree(tree)
        if isinstance(node, list):
            format_tree(node)

    return tree


def get_node(tree, node_name):
    ERROR = f"Nothing there with name - '{node_name}'"

    for node in tree:
        if get_name(node) == node_name:
            return node
        if isinstance(node[1], list):
            result_in_childs = get_node(get_children(node), node_name)
            if not isinstance(result_in_childs, Exception):
                return result_in_childs

    return Exception(ERROR)


def get_children(node: list):
    return node[1] if isinstance(node[1], list) else Exception("Child free")


def get_value(node: list):
    return node[1]


def get_name(node: list):
    return node[0]


def get_meta(node: list):
    return node[2]
