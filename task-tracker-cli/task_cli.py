import sys
from task_operations import add_task, update_task, delete_task
from task_status import mark_status, list_tasks


def task_cli() -> None:
    command = sys.argv[1]
    if command == "add":
        add_task(sys.argv[2])
    elif command == "update":
        update_task(sys.argv[2], sys.argv[3])
    elif command == "delete":
        delete_task(sys.argv[2])
    elif command == "mark-in-progress":
        mark_status(int(sys.argv[2]), "in-progress")
    elif command == "mark-done":
        mark_status(int(sys.argv[2]), "done")
    elif command == "list":
        list_tasks(sys.argv[2])
    else:
        print("Unknown command")


if __name__ == "__main__":
    task_cli()
