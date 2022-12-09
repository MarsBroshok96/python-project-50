from gendiff.tree_constructor import (get_meta, get_value, get_name, get_node)


def treat_value(value):
    """
    Return [complex value] if dict value is nested, else return value.
    """
    if isinstance(value, list):
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

    for node in [n for n in tree if get_meta(n)['diff_status'] in STAT]:
        stat = get_meta(node)['diff_status']
        dir_.append(get_name(node))
        path = '.'.join(dir_)
        if stat == 'look_inside':
            output.extend(form_plain(get_value(node), dir_))
            dir_ = dir_[:-1]
        elif get_meta(node)['diff_status'] == 'old_value':
            old_val = treat_value(get_value(node))
            new_val_node = get_node(tree, get_name(node), 'new_value')
            new_val = treat_value(get_value(new_val_node))
            output.append(STAT[stat].format(path=path,
                                            old_val=old_val,
                                            new_val=new_val
                                            ))
        else:
            val = treat_value(get_value(node))
            output.append(STAT[stat].format(path=path, val=val))
        dir_ = dir_[:-1]

    return output


def format(tree):
    """
    Main func to form correct output in plain format.
    """
    result = '\n'.join(form_plain(tree))
    result += '\n'

    return result
