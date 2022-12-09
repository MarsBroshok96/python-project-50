from gendiff.formatters import (stylish, plain, json_)

STYLES = {'stylish': stylish, 'plain': plain, 'json': json_}


def formatting(tree, style):

    return STYLES[style].format(tree)
