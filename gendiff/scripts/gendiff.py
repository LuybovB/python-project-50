import argparse


def main():
    parser = argparse.ArgumentParser(description='Your description of the script')

    # add other arguments
    parser.add_argument('path', help='Description of the path argument')

    args = parser.parse_args()


if __name__ == "__main__":
    main()
