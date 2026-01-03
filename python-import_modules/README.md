# Python - Import & Modules

This directory covers the basics of importing and using modules in Python, including built-in modules, user-defined modules, and handling module execution.

## Learning Objectives
- Understand how to import functions from another file
- Use the `__import__` function
- Differentiate between script execution and module import
- Handle command-line arguments with `sys.argv`
- Work with basic Python modules like `math`, `random`, etc.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.*
- All files should end with a new line
- The first line of all Python files should be `#!/usr/bin/python3`
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable
- Modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)

## Project Structure
- **0-add.py** – Import a simple function and print the result
- **1-calculation.py** – Perform calculations with imported functions
- **2-args.py** – Print the number of and list of arguments
- **3-infinite_add.py** – Add infinite numbers from command line
- **4-hidden_discovery.py** – Print all names defined by a compiled module
- **5-variable_load.py** – Import a variable from a file and print its value

## Usage
Each script can be run independently:
```bash
./0-add.py
