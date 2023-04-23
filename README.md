# My second step on python path.


### Tests and CC:
[![Actions Status](https://github.com/MarsBroshok96/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/MarsBroshok96/python-project-50/actions) ![example workflow](https://github.com/MarsBroshok96/python-project-50/actions/workflows/linter-and-tests.yml/badge.svg)
<a href="https://codeclimate.com/github/MarsBroshok96/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/c2ecb2ed70133fea33a6/maintainability" /></a>  <a href="https://codeclimate.com/github/MarsBroshok96/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/c2ecb2ed70133fea33a6/test_coverage" /></a>

### Built With
Languages, frameworks and libraries used in the implementation of the project:

[![](https://img.shields.io/badge/language-python-blue)](https://github.com/topics/python) [![](https://img.shields.io/badge/library-json-yellow)](https://github.com/topics/json) [![](https://img.shields.io/badge/library-pyyaml-red)](https://github.com/topics/pyyaml) [![](https://img.shields.io/badge/library-argparse-lightgrey)](https://github.com/topics/argparse)

### Dependencies
List of dependencies, without which the project code will not work correctly:
- python = "^3.10"
- pyyaml = "^6.0"

## Description
Difference Generator is a program that determines the difference between two data structures. A similar mechanism is used when outputting tests or when automatically tracking changes in configuration files.

To build a diff between two structures, many operations have to be done: reading files, parsing incoming data, building a tree of differences, and generating the necessary output.

**Utility features:**
- [X] Suppported file formats: YAML, JSON.
- [X] Report generation as plain text, structured text or JSON.
- [X] Can be used as CLI tool or external library.

### Summary
* [Description](#description)
* [Installation](#installation)
* [Usage](#usage)
  * [As external library](#as-external-library)
  * [As CLI tool](#as-cli-tool)
  * [Help](#help)
  * [Demo](#demo)
* [Development](#development)
  * [Dev Dependencies](#dev-dependencies)
  * [Root Structure](#root-structure)
___

## Installation

To work with the package, you need to clone the repository. This is done using the ```git clone``` command. Clone the project on the command line:

```bash
# clone via HTTPS:
>> git clone https://github.com/MarsBroshok96/python-project-50.git

# clone via SSH:
>> git clone git@github.com:MarsBroshok96/python-project-50.git
```

It remains to move to the directory and install the package:

```bash
>> cd python-project-50
>> make install
>> make build
>> make package-install
```

Finally, we can move on to using the project functionality!

___

## Usage

### As external library

```python
from gendiff import generate_diff
diff = generate_diff(file_path1, file_path2)
```

### As CLI tool

#### Help

The utility provides the ability to call the help command if you find it difficult to use:

```bash
>> gendiff --help
```
```bash
usage: gendiff [-h] [-f {stylish,json,plain}] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f {stylish,json,plain}, --format {stylish,json,plain}
                        set format of output (default: stylish)
```
#### Demo

Example of using package to generate diffs of two json/yaml files:
[![asciicast](https://asciinema.org/a/tKOqoN4fFRGBfAj23LCs6SdVI.svg)](https://asciinema.org/a/tKOqoN4fFRGBfAj23LCs6SdVI)

Package demonstration ('stylish' format)
[![asciicast](https://asciinema.org/a/rqCpdVzOF0LcoUe5v1fDJP1Rg.svg)](https://asciinema.org/a/rqCpdVzOF0LcoUe5v1fDJP1Rg)

Package demonstration ('plain' format)
[![asciicast](https://asciinema.org/a/517eQetiwLOCid6zJ7iAlUC43.svg)](https://asciinema.org/a/517eQetiwLOCid6zJ7iAlUC43)

Package demonstration ('json' format)
[![asciicast](https://asciinema.org/a/5g3ZJB0pMZu7UsL1EsCcIAP0m.svg)](https://asciinema.org/a/5g3ZJB0pMZu7UsL1EsCcIAP0m)


## Development

### Dev Dependencies

List of dev-dependencies:
- flake8 = "^6.0.0"
- pytest = "^7.2.0"
- pytest-cov = "^4.0.0"

### Root Structure

```bash
>> tree .
```
```bash
.
├── Makefile
├── README.md
├── coverage.xml
├── gendiff
│   ├── __init__.py
│   ├── __pycache__
│   ├── cli.py
│   ├── engine.py
│   ├── formatters
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── json_.py
│   │   ├── plain.py
│   │   └── stylish.py
│   ├── formatting.py
│   ├── parser.py
│   ├── scripts
│   │   ├── __init__.py
│   │   └── start_gendiff.py
│   └── tree_constructor.py
├── poetry.lock
├── pyproject.toml
├── setup.cfg
└── tests
    ├── __init__.py
    ├── __pycache__
    ├── fixtures
    │   ├── file1.json
    │   ├── file1.yaml
    │   ├── file2.json
    │   ├── file2.yml
    │   ├── result_json.json
    │   ├── result_plain
    │   └── result_stylish
    └── test_gendiff.py

```