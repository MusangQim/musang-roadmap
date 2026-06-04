# Task-Tracker-Cli
## Description

## Requirements

## Installation
If you wish to check basic syntax errors you can install flake8
```bash
pip install flake8

flake8 <file.py>
```
If you wish to check basic syntax errors you can install flake8
```bash
pip install mypy

python3 -m mypy <file.py>
```

## Usage

## Project Structure
- argv_parser.py - understanding on how CLI app receive the input() from terminal.
- json_handler.py - understanding on how read and write JSON file from scratch using native file system.
- task_model.py - construct tasks using dictionary as a part of data structures in Python and follow the required properties.
- task_operations.py - implementing CRUD operation (Create, Read, Update, Delete) into list of tasks dict.
- task_status.py - implementing status management and filtering (mark-done, mark-in-progress, mark-done, list)
- task_cli.py - combining all files from argv_parser until task_status to create Task Tracker CLI
