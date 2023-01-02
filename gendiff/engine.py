"""Base functions for gendiff"""

import copy
import os
from gendiff import parser
from gendiff.formatters.formatting import formatting
from gendiff.tree_constructor import (make_tree_dict, get_diff)


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

    file1 = save_bool_format(parser.parse_data(get_data(file_path1),
                                               get_format(file_path1)
                                               ))
    file2 = save_bool_format(parser.parse_data(get_data(file_path2),
                                               get_format(file_path2)
                                               ))

    diff_tree = make_tree_dict(get_diff(file1, file2), tree_type='diff')
    sorted_tree = make_tree_dict(get_sorted(diff_tree.get('children')),
                                 tree_type='sorted_diff')

    return formatting(sorted_tree.get('children'), format_name)


def get_data(file_path):
    """
    Get file path, return data from file.
    """
    data = open(file_path)

    return data


def get_format(file_path):
    """
    Get file path, return file extension.
    """
    extension = os.path.split(file_path)[1].split('.')[1]

    return extension


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
        if node.get('children'):
            node['children'] = get_sorted(node.get('children'))
    tree_c = sorted(tree_c, key=lambda _: _.get('name'))

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
        elif isinstance(file[key], (bool, type(None))):
            file[key] = CHANGE_COLLECTION[file[key]]

    return file
