"""Base functions for gendiff"""

import copy
from gendiff import parser
from gendiff.tree_constructor import (construct_1lvl_mutable_tree,
                                      get_name, get_value, get_meta)


PREFIX_RM = " - "
PREFIX_ADD = " + "
PREFIX_NTH = "   "
REMOVED_INFO = {'diff_status': PREFIX_RM, 'origin': 1}
ADDED_INFO = {'diff_status': PREFIX_ADD, 'origin': 2}
NON_CHANGED_INFO = {'diff_status': PREFIX_NTH, 'origin': 2}


def generate_diff(file_path1, file_path2):

    file1 = parser.parse_data(file_path1)
    file2 = parser.parse_data(file_path2)

    items_file1 = set(file1.items())
    items_file2 = set(file2.items())

    added_items = items_file2 - items_file1
    removed_items = items_file1 - items_file2
    non_changed_items = items_file1 & items_file2

    added_tree = construct_1lvl_mutable_tree(dict(added_items),
                                             common_meta=ADDED_INFO)
    removed_tree = construct_1lvl_mutable_tree(dict(removed_items),
                                               common_meta=REMOVED_INFO)
    non_changed_tree = construct_1lvl_mutable_tree(dict(non_changed_items),
                                                   common_meta=NON_CHANGED_INFO)

    diff_tree = copy.deepcopy(added_tree + removed_tree + non_changed_tree)
    sorted_tree = get_json_style(get_sorted(diff_tree))
    result = make_output_format(sorted_tree)

    return result


def get_sorted(tree: list):

    result = sorted(tree, key=lambda node: (get_name(node),
                                            get_meta(node)['origin']))
    return result


def get_json_style(tree: list):
    CHANGE_COLLECTION = {False: 'false', True: 'true'}

    for node in tree:
        if get_value(node) in CHANGE_COLLECTION:
            node[1] = CHANGE_COLLECTION[get_value(node)]
    return tree


def make_output_format(sorted_tree):
    def make_string_from_node(node):
        return '{0}{1}: {2}'.format(get_meta(node)["diff_status"],
                                    get_name(node), get_value(node))

    list_of_strings = [make_string_from_node(node) for node in sorted_tree]
    output = '{\n'
    output += '\n'.join(list_of_strings)
    output += '\n}\n'

    return output
