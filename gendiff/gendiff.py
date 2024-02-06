from gendiff.reader import read_file, get_format_file
from gendiff.parser import parse
from gendiff.data import build_diff_data
from gendiff.formatter.formatter import format_diff
from gendiff.formatter.formats import STYLISH


def load_and_parse_data(file_path, file_format):
    file_content = read_file(file_path)
    return parse(file_content, file_format)


def generate_diff(file_path1, file_path2, formatter=STYLISH):
    format1 = get_format_file(file_path1)
    format2 = get_format_file(file_path2)
    data1 = load_and_parse_data(file_path1, format1)
    data2 = load_and_parse_data(file_path2, format2)
    diff = build_diff_data(data1, data2)
    return format_diff(diff, formatter)
