from gendiff.formatters import (stylish, plain, json_)

STYLES = {'stylish': stylish, 'plain': plain, 'json': json_}


def formatting(tree, style):
    """
    Convert output formate in depend of selected style.

    Args:
        tree: tree (list of lists) with differences.
        style: one of supported formats: 'stylish', 'plain' or 'json'.
    Returns:
           String with diffs in selected style.
    """

    if style not in STYLES:
        raise Exception('Invalid style. Try one of: {0}'.format
                        (list(STYLES.keys())))

    return STYLES[style].format_(tree)
