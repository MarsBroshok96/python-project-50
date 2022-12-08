from gendiff.formatters import stylish

STYLES = {'stylish': stylish}


def formatting(tree, style):

    return STYLES[style].format(tree)
