"""
Module that contain constructor and selectors of  mutable tree abstraction.
"""


def make_tree_list(old: dict, new: dict):
    """
    Take two dicts and construct tree (list of lists) with differences in meta:
    diff_status may be:
    'look_inside' - nested node with diffs inside;
    'removed' - in first dict, but not in second;
    'added' - in second dict, but not in first;
    'old' - same in first and second dicts;
    'old_value' - old value, but was changed in second dict;
    'new_value' - new value that replaced old value from first dict.

    Args:
        old: first python dict,
        new: second python dict.
    Returns:
           diffs: tree (list of lists) with differences.
    """
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
            diffs.append([key, make_tree_list(old_value, new_value),
                          {'diff_status': 'look_inside'}
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
    """
    Treat (with mutation) nested value to tree (list of lists) format
    with selected 'diff_status' in meta.

    Args:
        val: nested list.
        diff_status: meta info for all nested values ('' by default).
    Returns:
           val: treated val
    """
    if isinstance(val, dict):
        formated_val = [[k, treat_val(v)] for k, v in val.items()]
        for sub_val in formated_val:
            sub_val.append({'diff_status': diff_status})
        return formated_val
    return val


def get_node(tree, name, stat):
    """
    Base selector to get node(list) by name and diff_status.
    """
    ERROR = f"Nothing there with name - '{name}' and status - '{stat}'"

    for node in tree:
        if get_name(node) == name and get_meta(node)['diff_status'] == stat:
            return node
        if isinstance(node[1], list):
            result_in_childs = get_node(get_children(node), name, stat)
            if not isinstance(result_in_childs, Exception):
                return result_in_childs

    return Exception(ERROR)


def get_children(node: list):
    """
    Base selector to get children (list of lists) by node.
    """
    return node[1] if isinstance(node[1], list) else Exception("Child free")


def get_value(node: list):
    """
    Base selector to get value by node.
    """
    return node[1]


def get_name(node: list):
    """
    Base selector to get name by node.
    """
    return node[0]


def get_meta(node: list):
    """
    Base selector to get meta ('diff_status' for example) by node.
    """
    return node[2]
