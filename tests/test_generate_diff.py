from gendiff.diff_with_formatter import generate_diff
import os

file1_path = os.path.join(os.path.dirname(__file__), "fixtures", "file1.json")
file2_path = os.path.join(os.path.dirname(__file__), "fixtures", "file2.json")
file11_path = os.path.join(os.path.dirname(__file__), "fixtures", "file1.yml")
file22_path = os.path.join(os.path.dirname(__file__), "fixtures", "file2.json")

test_data = [
    (file1_path, file2_path, "fixtures/file3.json"),
    (file1_path, file2_path, "fixtures/file3.yml"),
]


def test_generate_diff():
    for filepath1, filepath2, expected_file in test_data:
        diff = generate_diff(filepath1, filepath2)
