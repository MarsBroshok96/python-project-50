def stringify_dict(data, indent: int):
    """
    Convert dict to strings with choosen indent.
    """
    if not isinstance(data, dict):
        return data
    output = ["{"]
    for key, val in data.items():
        output.append(f"\n{'  '* indent}{key}: "
                      f"{stringify_dict(val, indent + 2)}"
                      )
    output.append(f"\n{'  ' * (indent - 2)}}}")

    return ''.join(output)


def form_stylish(tree, depth=1):
    """
    Gen strings with differences and correct indent.

    Args:
        tree: list of lists with differences,
        depth: correct indent (1 by default).
    Returns:
           output: Strings with correct indent for stylish format.
    """
    STAT = {'old_value': '- ',
            'new_value': '+ ',
            'removed': '- ',
            'added': '+ ',
            'unchanged': '  ',
            'look_inside': '  '
            }

    def make_str(node, depth):
        """
        Convert every node(list) to string with indent depends on depth.
        """
        def treat_node(node, depth):
            """
            Return form_stylish(value) if value is list, else return value.
            """
            if not node.get('children'):
                if isinstance(node.get('value'), dict):

                    return stringify_dict(node.get('value'), depth + 1)

                return node.get('value')

            return '{{\n{0}\n{1}}}'.format(form_stylish(node.get('children'),
                                                        depth
                                                        ),
                                           '  ' * (depth - 1)
                                           )

        return '{0}{1}{2}: {3}'.format('  ' * depth,
                                       STAT[node.get('type')],
                                       node.get('name'),
                                       treat_node(node, depth + 2)
                                       )

    list_of_str = [make_str(node, depth) for node in tree]
    output = '\n'.join(list_of_str)

    return output


def format(tree):
    """
    Main func to form correct output in stylish format.
    """
    return f"{{\n{form_stylish(tree)}\n}}"
