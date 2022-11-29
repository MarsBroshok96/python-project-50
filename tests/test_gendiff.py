import pytest
from gendiff import engine


json1 = "tests/fixtures/file1.json"
json2 = "tests/fixtures/file2.json"
result1 = "tests/fixtures/result1.json"
yaml1 = "tests/fixtures/file1.yaml"
yaml2 = "tests/fixtures/file2.yml"

@pytest.mark.parametrize(
        ("file_path1", "file_path2", "expected"),[(json1, json2, result1),
                                                  (yaml1, yaml2, result1)]
        )

def test_generate_diff(file_path1, file_path2, expected):
    with open(expected, "r") as correct:
        assert engine.generate_diff(file_path1, file_path2) == correct.read()
