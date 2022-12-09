from gendiff.formatters import (stylish, plain)

STYLES = {'stylish': stylish, 'plain': plain}


def formatting(tree, style):

    return STYLES[style].format(tree)
