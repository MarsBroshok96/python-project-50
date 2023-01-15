"""
Module that contain constructor and selectors of mutable tree abstraction.
"""


def make_tree_dict(diff, tree_type: str):
    """
    Add tree_type to diff_tree.
    """
    return {'type': tree_type, 'children': diff}


def get_diff(old: dict, new: dict):
    """
    Take two dicts and construct tree (list of objects(children))
    with differences in meta(type) and sorted by 'name':
    type may be:
    'look_inside' - nested node with diffs inside;
    'removed' - in first dict, but not in second;
    'added' - in second dict, but not in first;
    'unchanged' - same in first and second dicts;
    'changed', that contents two different values:
       'old_value' - old value that was changed in second dict;
       'new_value' - new value that replaced old value from first dict.

    Args:
        old: first python dict,
        new: second python dict.
    Returns:
           diffs: tree (list of objects) with differences.
    """
    diffs = []
    old_keys = set(old.keys())
    new_keys = set(new.keys())
    keys = old_keys | new_keys

    for key in sorted(keys):
        if key not in old_keys:
            diffs.append({'type': 'added', 'name': key, 'value': new[key]})

        elif key not in new_keys:
            diffs.append({'type': 'removed', 'name': key, 'value': old[key]})

        else:
            old_value = old[key]
            new_value = new[key]
            if isinstance(old[key], dict) and isinstance(new[key], dict):
                diffs.append({'type': 'look_inside',
                              'name': key,
                              'children': get_diff(old_value, new_value)
                              })
            else:
                if new_value == old_value:
                    diffs.append({'type': 'unchanged',
                                  'name': key,
                                  'value': old_value
                                  })
                else:
                    diffs.append({'type': 'changed',
                                  'name': key,
                                  'old_value': old_value,
                                  'new_value': new_value
                                  })

    return diffs


def get_node(tree, name, type_):
    """
    Base selector to get node(list) by name and diff_status.
    """
    ERROR = F"Nothing there with name - '{name}' and type '{type_}'"

    for node in tree:
        if node.get('name') == name and node.get('type') == type_:
            return node
        if node.get('children'):
            result_in_childs = get_node(node.get('children'), name, type_)
            if not isinstance(result_in_childs, Exception):
                return result_in_childs

    return Exception(ERROR)
