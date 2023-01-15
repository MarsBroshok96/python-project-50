"""Base functions for gendiff"""


import os
from gendiff import parser
from gendiff.formatting import formatting
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

    file1 = parser.parse_data(get_data(file_path1),
                              get_format(file_path1)
                              )
    file2 = parser.parse_data(get_data(file_path2),
                              get_format(file_path2)
                              )

    diff_tree = make_tree_dict(get_diff(file1, file2), tree_type='diff')
    return formatting(diff_tree, format_name)


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
