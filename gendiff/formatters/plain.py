# from gendiff.tree_constructor import get_node
from gendiff.formatters.stylish import save_bool_format


def treat_value(value):
    """
    Return [complex value] if dict value is nested, else return value.
    """
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, (int, float, bool, type(None))):
        return save_bool_format(value)
    else:
        return f"'{value}'"


def format_(tree, dir_=None):
    """
    Form list of strings with tree (list of lists) of differences.
    """
    STAT = {'changed': "Property '{path}' was updated."
                       " From {old_val} to {new_val}",
            'removed': "Property '{path}' was removed",
            'added': "Property '{path}' was added with value: {val}",
            'look_inside': ''
            }
    if isinstance(tree, dict) and tree['type'] == 'diff':

        return '\n'.join(format_(tree['children']))

    else:
        if dir_ is None:
            dir_ = []
        output = []

        for node in [_ for _ in tree if _.get('type') in STAT]:
            stat = node.get('type')
            dir_.append(node.get('name'))
            path = '.'.join(dir_)
            if stat == 'look_inside':
                output.extend(format_(node.get('children'), dir_))
                dir_ = dir_[:-1]
            elif node.get('type') == 'changed':
                old_val = treat_value(node.get('old_value'))
                new_val = treat_value(node.get('new_value'))
                output.append(STAT[stat].format(path=path,
                                                old_val=old_val,
                                                new_val=new_val
                                                ))
            else:
                val = treat_value(node.get('value'))
                output.append(STAT[stat].format(path=path, val=val))
            dir_ = dir_[:-1]

        return output
