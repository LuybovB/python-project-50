#!/usr/bin/env python
import os


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def get_format_file(file_path):
    root, extension = os.path.splitext(file_path)
    if extension in ('.yaml', '.yml'):
        return 'yaml'
    elif extension == '.json':
        return 'json'
