import pytest
from gendiff import engine


json1 = "tests/fixtures/file1.json"
json2 = "tests/fixtures/file2.json"
h_json1 = "tests/fixtures/hard1.json"
h_json2 = "tests/fixtures/hard2.json"
r1 = "tests/fixtures/result1"
r2 = "tests/fixtures/hard_result_stylish"
r3 = "tests/fixtures/hard_result_plain"
r4 = "tests/fixtures/hard_result_json.json"
yaml1 = "tests/fixtures/file1.yaml"
yaml2 = "tests/fixtures/file2.yml"
h_yaml1 = "tests/fixtures/hard1.yaml"
h_yaml2 = "tests/fixtures/hard2.yml"


@pytest.mark.parametrize(("p1", "p2", "style", "expected"),
                         [(json1, json2, 'stylish', r1),
                          (yaml1, yaml2, 'stylish', r1),
                          (h_json1, h_json2, 'stylish', r2),
                          (h_yaml1, h_yaml2, 'stylish', r2),
                          (h_json1, h_json2, 'plain', r3),
                          (h_yaml1, h_yaml2, 'plain', r3),
                          (h_json1, h_json2, 'json', r4),
                          (h_yaml1, h_yaml2, 'json', r4)]
                         )
def test_generate_diff(p1, p2, style, expected):
    with open(expected, "r") as correct:
        assert engine.generate_diff(p1, p2, style) == correct.read()
