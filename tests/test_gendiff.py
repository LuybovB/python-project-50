import pytest
from gendiff.gendiff import generate_diff
from gendiff.formatter.formats import JSON, STYLISH, PLAIN


@pytest.mark.parametrize('filepath1, filepath2, format_name, answer', [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json',
     STYLISH, 'tests/fixtures/answer_stylish_flat'),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml',
     STYLISH, 'tests/fixtures/answer_stylish_flat'),
    ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml',
     STYLISH, 'tests/fixtures/answer_stylish_flat'),
    ('tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json',
     STYLISH, 'tests/fixtures/answer_stylish_nested'),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2_nested.yaml',
     STYLISH, 'tests/fixtures/answer_stylish_nested'),
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json',
     PLAIN, 'tests/fixtures/answer_plain_flat'),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml',
     PLAIN, 'tests/fixtures/answer_plain_flat'),
    ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml',
     PLAIN, 'tests/fixtures/answer_plain_flat'),
    ('tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json',
     PLAIN, 'tests/fixtures/answer_plain_nested'),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2_nested.yaml',
     PLAIN, 'tests/fixtures/answer_plain_nested'),
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json',
     JSON, 'tests/fixtures/answer_plain_flat'),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml',
     JSON, 'tests/fixtures/answer_plain_flat'),
    ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml',
     JSON, 'tests/fixtures/answer_plain_flat'),
    ('tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json',
     JSON, 'tests/fixtures/answer_json_nested'),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2_nested.yaml',
     JSON, 'tests/fixtures/answer_json_nested'),
])
def test_generate_diff(filepath1, filepath2, format_name, answer):
    assert generate_diff(filepath1, filepath2, format_name)
