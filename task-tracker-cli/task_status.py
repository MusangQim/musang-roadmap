from json_handler import load_tasks
from task_operations import save_tasks, add_task
import datetime
import pyfiglet


def mark_status(id, new_status):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == id:
            found = True
            task["status"] = new_status
            task["updatedAt"] = datetime.datetime.now().strftime("%c")
            print("STATUS: The status successfully updated!")
            break
    if not found:
        print("Error: No status updated")
        return
    save_tasks(tasks)


def list_tasks(filter=None):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!!!")
        return
    # Header Output
    banner = pyfiglet.figlet_format("> Task_Tracker <", font="slant")
    print(banner)
    tag = "---------- created by MusangQim ----------\n"
    print(tag.center(70))
    print(f"{'ID':<5} {'Description':<25} {'Status':<15} {'Created'}")
    # Divider
    print("-" * 80)
    if filter is None:
        for task in tasks:
            format = (
                  f"{task['id']:<6}"
                  f"{task['description']:<26}"
                  f"{task['status']:<16}"
                  f"{task['createdAt']}"
            )
            print(format)
    else:
        for task in tasks:
            if task["status"] == filter:
                format = (
                  f"{task['id']:<6}"
                  f"{task['description']:<26}"
                  f"{task['status']:<16}"
                  f"{task['createdAt']}"
                )
            print(format)


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
