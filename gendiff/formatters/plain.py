from gendiff.tree_constructor import get_node


def treat_value(value):
    """
    Return [complex value] if dict value is nested, else return value.
    """
    if isinstance(value, dict):
        return '[complex value]'
    elif value in ('true', 'false', 'null') or isinstance(value, (int, float)):
        return value
    else:
        return f"'{value}'"


def form_plain(tree, dir_=None):
    """
    Form list of strings with tree (list of lists) of differences.
    """
    STAT = {'old_value': "Property '{path}' was updated."
                         " From {old_val} to {new_val}",
            'removed': "Property '{path}' was removed",
            'added': "Property '{path}' was added with value: {val}",
            'look_inside': ''
            }
    if dir_ is None:
        dir_ = []
    output = []

    for node in [_ for _ in tree if _.get('type') in STAT]:
        stat = node.get('type')
        dir_.append(node.get('name'))
        path = '.'.join(dir_)
        if stat == 'look_inside':
            output.extend(form_plain(node.get('children'), dir_))
            dir_ = dir_[:-1]
        elif node.get('type') == 'old_value':
            old_val = treat_value(node.get('value'))
            new_val_node = get_node(tree, node.get('name'), 'new_value')
            new_val = treat_value(new_val_node.get('value'))
            output.append(STAT[stat].format(path=path,
                                            old_val=old_val,
                                            new_val=new_val
                                            ))
        else:
            val = treat_value(node.get('value'))
            output.append(STAT[stat].format(path=path, val=val))
        dir_ = dir_[:-1]

    return output


def format(tree):
    """
    Main func to form correct output in plain format.
    """
    result = '\n'.join(form_plain(tree))

    return result
