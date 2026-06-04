# Task-Tracker-Cli
## Description

## Requirements
- Python

## Installation
1. Clone this repository first
```bash
git clone https://github.com/MusangQim/musang-task_tracker
```

2. Navigate to project folder
```bash
cd musang-task_tracker
```

3. There a lot of file Python in the folder. Run using python3
```bash
python3 <file.py>
```

4. If you want to check basic syntax errors, you can install flake8
```bash
pip install flake8
flake8 <file.py>
```

5. If you want to verify data types or static type, you can install flake8
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
