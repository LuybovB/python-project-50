import os


def read_file(filepath):
    absolute_path = os.path.abspath(filepath)
    with open(absolute_path, 'r') as file:
        return file.read()


def get_format(filepath):
    root, ext = os.path.splitext(filepath)
    if ext == '.yaml' or ext == '.yml':
        return 'yaml'
    elif ext == '.json':
        return 'json'
