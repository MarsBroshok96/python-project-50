import json
import yaml

EXTENSIONS = {'json': json.load,
              'yaml': yaml.safe_load,
              'yml': yaml.safe_load}


def parse_data(data, extension):
    """
    Get file data and extension, Select a parser
    and parse in depend on file extention.

    Args:
        data: data from file
        extension: file extension
    Returns:
           Python dict
    """
    if extension in EXTENSIONS:
        return EXTENSIONS[extension](data)

    raise Exception('Invalid extension. Try: {0}'.format
                    (list(EXTENSIONS.keys())))
