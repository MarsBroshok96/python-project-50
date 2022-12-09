from gendiff.tree_constructor import (get_meta, get_value, get_name)


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
            'removed': '- ',
            'added': '+ ',
            'new_value': '+ ',
            'old': '  ',
            '': '  ',
            'look_inside': '  '
            }

    def make_str(node, depth):
        """
        Convert every node(list) to string with indent depends on depth.
        """
        def treat_value(node, depth):
            """
            Return form_stylish(value) if value is list, else return value.
            """
            if not isinstance(node, list):

                return node

            return f"{{\n{form_stylish(node, depth)}\n{'  '*(depth - 1)}}}"

        return '{0}{1}{2}: {3}'.format('  ' * depth,
                                       STAT[get_meta(node)["diff_status"]],
                                       get_name(node),
                                       treat_value(get_value(node), depth + 2)
                                       )

    list_of_str = [make_str(node, depth) for node in tree]
    output = '\n'.join(list_of_str)

    return output


def format(tree):
    """
    Main func to form correct output in stylish format.
    """
    return f"{{\n{form_stylish(tree)}\n}}\n"
