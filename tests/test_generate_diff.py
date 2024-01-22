import pytest
from gendiff.diff_with_formatter import generate_diff

test_data = [
    ("fixtures/file1.json", "fixtures/file2.json", "fixtures/file3.json")
]


def test_generate_diff():
    for filepath1, filepath2, expected_file in test_data:
        diff = generate_diff(filepath1, filepath2)
