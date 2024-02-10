from gendiff.reader import read_file, get_format
from gendiff.parser import parse
from gendiff.data import data
from gendiff.formatter.formatter import format_diff
from gendiff.formatter.formats import STYLISH


def generate_diff(filepath1, filepath2, formatter=STYLISH):
    format1 = get_format(filepath1)
    format2 = get_format(filepath2)
    data1 = parse(read_file(filepath1), format1)
    data2 = parse(read_file(filepath2), format2)
    diff = data(data1, data2)
    return format_diff(diff, formatter)
