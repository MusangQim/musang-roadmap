# Task-Tracker-Cli
A simple Command Line Interface (CLI) application for tracking and managing daily tasks. Users can create, update, delete, and monitor task status such as todo, in-progress, and done. The project demonstrates file handling, user input processing, and basic data persistence in a CLI environment.

## Installation
1. Clone this repository first
```bash
git clone https://github.com/MusangQim/musang-task_tracker
```

2. Navigate to project folder
```bash
cd musang-task_tracker/task-tracker-cli
```

3. Run the main CLI app
```bash
python3 task_cli.py
```

4. If you want to check basic syntax errors, you can install flake8
```bash
pip install flake8
flake8 <file.py>
```

5. If you want to verify data types or static type, you can install mypy
```bash
pip install mypy
python3 -m mypy <file.py>
```

## Usage
```python
# Add Task
 # Put " " if argument more than two (Example: "Jog and Breakfast")
python3 task_cli.py add "<description>"

# Update Task
 # Choose which ID you want and update with new description
python3 task_cli.py update <id> "<description>"


# Delete Task
 # Choose which ID you want to delete
python3 task_cli.py delete <id>

# Mark Status
 # Mark the task using "todo", "in-progress" and "done"
python3 task_cli.py mark-in-progress <id>
python3 task_cli.py mark-done <id>

# List All Tasks
python3 task_cli.py list

# List Specific Task
 # List tasks according to the status
python3 task_cli.py list todo
python3 task_cli.py list in-progress
python3 task_cli.py list done
```

## Project Structure
- argv_parser.py - understanding on how CLI app receive the input() from terminal.
- json_handler.py - understanding on how read and write JSON file from scratch using native file system.
- task_model.py - construct tasks using dictionary as a part of data structures in Python and follow the required properties.
- task_operations.py - implementing CRUD operation (Create, Read, Update, Delete) into list of tasks dict.
- task_status.py - implementing status management and filtering (mark-done, mark-in-progress, mark-done, list)
- task_cli.py - combining all files from argv_parser until task_status to create Task Tracker CLI

## Source
Project idea from [roadmap.sh](https://roadmap.sh/projects/task-tracker)