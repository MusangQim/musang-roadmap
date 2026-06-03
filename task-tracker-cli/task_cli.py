import sys
from task_operations import add_task, update_task, delete_task
from task_status import mark_status, list_tasks


def task_cli() -> None:
    # No Argument
    if len(sys.argv) < 2:
        print("Usage: python3 task_cli.py <command>")
        return
    command = sys.argv[1]
    # Add
    if command == "add":
        if len(sys.argv) < 3:
            print('Usage: python3 task_cli.py add "<description>"')
            return
        add_task(sys.argv[2])
    # Update
    elif command == "update":
        if len(sys.argv) < 3 or len(sys.argv) < 4:
            print("Usage: python3 task_cli.py update <id> <new_description>")
            return
        update_task(int(sys.argv[2]), sys.argv[3])
    # Delete
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python3 task_cli.py delete <id>")
            return
        try:
            delete_task(int(sys.argv[2]))
        except ValueError as e:
            print(f"Error: ID must in integer number: {e}")
    # Mark In-Progress
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: python3 task_cli.py mark-in-progress <id>")
            return
        try:
            mark_status(int(sys.argv[2]), "in-progress")
        except ValueError as e:
            print(f"Error: ID must in integer number: {e}")
    # Mark Done
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: python3 task_cli.py mark-done <id>")
            return
        try:
            mark_status(int(sys.argv[2]), "done")
        except ValueError as e:
            print(f"Error: ID must in integer number: {e}")
    # Show List All
    elif command == "list":
        if len(sys.argv) >= 3:
            filter = sys.argv[2]
            # Valid for Done, Todo, In-Progress
            valid = ["done", "todo", "in-progress"]
            if filter not in valid:
                print("Error: Invalid Status")
                print(" Use: 'done' or 'todo' or 'in-progress'")
                return
            list_tasks(filter)
        else:
            list_tasks()
    else:
        print("Unknown command")


if __name__ == "__main__":
    task_cli()
