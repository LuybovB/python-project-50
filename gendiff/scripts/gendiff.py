
import argparse

from gendiff.gendiff import generate_diff
from gendiff.formatter.formats import STYLISH, PLAIN, JSON


def parse_command_line_args():
    parser = argparse.ArgumentParser(
        usage='gendiff [-h] [-f FORMAT] first_file second_file',
        description='Compares two configuration '
                    'files and shows a difference'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        choices=[STYLISH, PLAIN, JSON],
        default=STYLISH,
        help='set format of output (default: "stylish")'
    )
    return parser.parse_args()


def main():
    args = parse_command_line_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
