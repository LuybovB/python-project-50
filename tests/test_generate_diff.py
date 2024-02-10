import pytest
from gendiff.gendiff import generate_diff
import re

test_data = [("tests/fixtures/file1.json", "tests/fixtures/file2.json",
             "tests/fixtures/answer_stylish_flat", "stylish"),
             ("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml",
             "tests/fixtures/answer_stylish_flat", "stylish"),
             ("tests/fixtures/file1_nested.json",
              "tests/fixtures/file2_nested.json",
             "tests/fixtures/answer_stylish_nested", "stylish"),
             ("tests/fixtures/file1_nested.yaml",
              "tests/fixtures/file2_nested.yaml",
             "tests/fixtures/answer_stylish_nested", "stylish"),
             ("tests/fixtures/file1.json", "tests/fixtures/file2.json",
              "tests/fixtures/answer_plain_flat", "plain"),
             ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml',
              'tests/fixtures/answer_plain_flat', "plain"),
             ('tests/fixtures/file1_nested.json',
              'tests/fixtures/file2_nested.json',
              'tests/fixtures/answer_plain_nested', "plain"),
             ('tests/fixtures/file1.json', 'tests/fixtures/file2.json',
              'tests/fixtures/answer_json_flat', "json"),
             ('tests/fixtures/file1_nested.json',
              'tests/fixtures/file2_nested.json',
              'tests/fixtures/answer_json_nested', "json"),
             ('tests/fixtures/file1_nested.yaml',
              'tests/fixtures/file2_nested.yaml',
              'tests/fixtures/answer_json_nested', "json"),
             ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml",
              "tests/fixtures/answer_stylish_flat", "stylish"),
             ]


@pytest.mark.parametrize("filepath1, filepath2, expected, format", test_data)
def test_generate_diff(filepath1, filepath2, expected, format):
    diff = generate_diff(filepath1, filepath2, format)
    with open(expected, 'r') as f:
        ans = f.read()
    diff = re.sub(r'\s+', ' ', diff.strip())
    ans = re.sub(r'\s+', ' ', ans.strip())

    assert diff == ans
