import sys
from task_operations import add_task, update_task, delete_task
from task_status import mark_status, list_tasks


def task_cli() -> None:
    command = sys.argv[1]
    id_input = int(sys.argv[2])
    if command == "add":
        add_task(sys.argv[2])
    elif command == "update":
        update_task(id_input, sys.argv[3])
    elif command == "delete":
        delete_task(id_input)
    elif command == "mark-in-progress":
        mark_status(id_input, "in-progress")
    elif command == "mark-done":
        mark_status(id_input, "done")
    elif command == "list":
        list_tasks(sys.argv[2])
    else:
        print("Unknown command")


if __name__ == "__main__":
    task_cli()
