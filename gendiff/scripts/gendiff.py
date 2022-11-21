"""Any info placeholder"""
import argparse


def main():
    """Name as main"""
    DESCRIPTION = "Compares two configuration files and shows a difference."
    parser = argparse.ArgumentParser(description = DESCRIPTION)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    print(args.first_file)



if __name__ =='__main__':
    main()
