"""
Program returns differences between file1 and file2
"""


from gendiff.cli import parse_args
from gendiff.engine import generate_diff


def main():
    """Name as main"""
    path_file1, path_file2, format_name = parse_args()

    print(generate_diff(path_file1, path_file2, format_name))


if __name__ == '__main__':
    main()
