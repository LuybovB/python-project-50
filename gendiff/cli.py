import argparse


def generate_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='first file to compare')
    parser.add_argument('second_file', help='second file to compare')
    parser.add_argument(
        '-o', '--output-format', dest='output_format',
        default='plain', help='set format of output'
    )
    return parser


def print_help(parser):
    help_str = parser.format_help()
    print(help_str)
