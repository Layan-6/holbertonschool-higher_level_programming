# Python - Test-Driven Development

This directory introduces Test-Driven Development (TDD) in Python using the `doctest` and `unittest` frameworks. The focus is on writing tests before implementation and ensuring code correctness and documentation.

## Learning Objectives
- Understand the concept of Test-Driven Development (TDD)
- Write documentation for modules and functions using docstrings
- Use `doctest` to embed tests in documentation
- Use `unittest` to create and run test suites
- Handle edge cases and exceptions in tests
- Apply TDD to real Python functions

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.*
- All files should end with a new line
- The first line of all Python files should be `#!/usr/bin/python3`
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable
- Modules and functions must have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Test files should be inside a folder named `tests` and use the `.txt` extension for doctests

## Project Structure
- **0-add_integer.py** – Add two integers with validation
- **tests/0-add_integer.txt** – Doctest for `add_integer`
- **2-matrix_divided.py** – Divide all elements of a matrix
- **tests/2-matrix_divided.txt** – Doctest for `matrix_divided`
- **3-say_my_name.py** – Print "My name is ..."
- **tests/3-say_my_name.txt** – Doctest for `say_my_name`
- **4-print_square.py** – Print a square with `#`
- **tests/4-print_square.txt** – Doctest for `print_square`
- **5-text_indentation.py** – Print text with newlines after `.`, `?`, and `:`
- **tests/5-text_indentation.txt** – Doctest for `text_indentation`
- **6-max_integer.py** – Find the max integer in a list (provided)
- **tests/6-max_integer_test.py** – Unittest for `max_integer`

## Usage
### Running doctests:
```bash
python3 -m doctest -v ./tests/0-add_integer.txt
