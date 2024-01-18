from gendiff.diff_with_formatter import generate_diff
from gendiff.cli import generate_parser


def main():
    parser = generate_parser()
    args = parser.parse_args()
    if args.first_file and args.second_file:
        print(generate_diff(args.first_file, args.second_file))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
