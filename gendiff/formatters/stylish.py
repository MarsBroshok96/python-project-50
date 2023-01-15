
def stringify(data, depth: int):
    """
    Convert data to strings with correct indent.
    """
    if not isinstance(data, dict):

        return save_bool_format(data)

    int_indent = build_indent(depth + 1)
    ext_indent = build_indent(depth)
    strings = ['{']

    for key, val in data.items():
        strings.append(f"\n{int_indent}  {key}: "
                       f"{stringify(val, depth + 1)}"
                       )
    strings.append(f"\n  {ext_indent}}}")

    return ''.join(strings)


def build_indent(depth):
    """
    Gen correct indent depend on current node`s depth.
    """
    return ' ' * (depth * 4 - 2)


def format_(tree, depth=0):
    """
    Convert tree with differences to str in stylish format and correct indent.
    Args:
        tree: list of objects with differences,
        depth: current node`s depth (0 by default).
    Returns:
        output: Str in stylish format or exception if diff_tree is incorrect.
    """
    STAT = {'old_value': '- ',
            'new_value': '+ ',
            'removed': '- ',
            'added': '+ ',
            'unchanged': '  ',
            'look_inside': '  '
            }
    indent = build_indent(depth)

    if tree['type'] == 'diff':
        lines = map(lambda child: format_(child, depth + 1),
                    tree.get('children')
                    )
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'

    elif tree['type'] == 'look_inside':
        lines = map(lambda child: format_(child, depth + 1),
                    tree.get('children')
                    )
        result = '\n'.join(lines)
        output = (f"{indent}{STAT[tree['type']]}{tree['name']}:"
                  f" {{\n{result}\n{indent}  }}"
                  )

        return output

    elif tree['type'] in ('added', 'removed', 'unchanged'):
        output = (f"{indent}{STAT[tree['type']]}{tree['name']}:"
                  f" {stringify(tree.get('value'), depth)}"
                  )

        return output

    elif tree['type'] == 'changed':
        output = (f"{indent}{STAT['old_value']}{tree['name']}:"
                  f" {stringify(tree.get('old_value'), depth)}\n"
                  f"{indent}{STAT['new_value']}{tree['name']}:"
                  f" {stringify(tree.get('new_value'), depth)}"
                  )

        return output

    raise Exception('Ivalid node`s type.')


def save_bool_format(data):
    """
    Change bool-types values to it source (json/yaml) format.

    Args:
        file: data in python format.
    Returns:
           file: data in json/yaml format.
    """
    CHANGE_COLLECTION = {False: 'false', True: 'true', None: 'null'}

    if data in CHANGE_COLLECTION:

        return CHANGE_COLLECTION[data]

    return data
