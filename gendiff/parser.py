import json
import yaml
import os

EXTENSIONS = {'json': json.load,
              'yaml': yaml.safe_load,
              'yml': yaml.safe_load}


def parse_data(path_to_file):
    """
    Gets file path, Selects a parser and parse in depend on file extention
    Returns: python dict
    """
    file = open(path_to_file)

    extension = os.path.split(path_to_file)[1].split('.')[1]

    if extension in EXTENSIONS:
        return EXTENSIONS[extension](file)

    raise Exception('Invalid extension. Try: {0}'.format
                    (list(EXTENSIONS.keys())))