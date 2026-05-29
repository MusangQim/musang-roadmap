from json_handler import load_tasks
from task_operations import save_tasks, add_task
import datetime


def mark_status(id, new_status):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == id:
            found = True
            task["status"] = new_status
            task["updatedAt"] = datetime.datetime.now().strftime("%c")
            print("Successfully update the status!")
            break
    if not found:
        print("Error")
        return
    save_tasks(tasks)


def list_tasks(filter=None):
    tasks = load_tasks()
    if filter is None:
        print(tasks)
    else:
        for task in tasks:
            if task["status"] == filter:
                print(task)


def main() -> None:
    add_task("Beli roti")
    add_task("Solat")
    mark_status(1, "in-progress")
    mark_status(1, "done")
    mark_status(99, "done")
    list_tasks()
    list_tasks("done")


if __name__ == "__main__":
    main()
