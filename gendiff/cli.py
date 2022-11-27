"""
CLi template for gendiff programm
"""


import argparse


def parse_args():
    """Name as main"""
    DESCRIPTION = "Compares two configuration files and shows a difference."
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    return args.first_file, args.second_file
