"""Base functions for gendiff"""

import copy
from gendiff import parser
from gendiff.formatters.formatting import formatting
from gendiff.tree_constructor import (make_tree_list,
                                      get_name, get_value, get_meta)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """
    Find difference of two files (changes from first file to the second).

    Args:
        file_path1: dir path to first,
        file_path2: dir path to second,
        format_name: format of output ('stylish' by default)
    Returns:
           String with difference in selected format.
    """

    file1 = save_bool_format(parser.parse_data(file_path1))
    file2 = save_bool_format(parser.parse_data(file_path2))

    diff_tree = make_tree_list(file1, file2)
    sorted_tree = get_sorted(diff_tree)

    return formatting(sorted_tree, format_name)


def get_sorted(tree: list):
    """
    Sort elements (w/o mutation) by name in all tree levels.
    If threre are nodes with same name in level,
    sort by origin (first file priority).

    Args:
        tree: list, constructed by tree_constructor
    Returns:
           tree_c: sorted deep copy of tree
    """
    tree_c = copy.deepcopy(tree)
    for node in tree_c:
        if isinstance(get_value(node), list):
            node[node.index(get_value(node))] = get_sorted(get_value(node))
    tree_c = sorted(tree_c,
                    key=lambda n: (get_name(n),
                                   get_meta(n)['diff_status'] == 'new_value'
                                   )
                    )

    return tree_c


def save_bool_format(file: dict):
    """
    Change bool-types values to it source (json/yaml) format.

    Args:
        file: python dict.
    Returns:
           file: python dict after change.
    """
    CHANGE_COLLECTION = {False: 'false', True: 'true', None: 'null'}

    for key in file.keys():
        if isinstance(file[key], dict):
            file[key] = save_bool_format(file[key])
        elif file[key] in CHANGE_COLLECTION:
            file[key] = CHANGE_COLLECTION[file[key]]

    return file
