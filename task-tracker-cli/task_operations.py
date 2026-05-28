import json
import datetime
from json_handler import load_tasks
from task_model import create_task


def save_tasks(tasks):
    with open("tasks.json", 'w') as file:
        json.dump(tasks, file)


def add_task(description):
    tasks = load_tasks()
    id = len(tasks) + 1
    new_task = create_task(id, description)
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {id})")


def update_task(id, description):
    tasks = load_tasks()
    update = False
    for task in tasks:
        if task["id"] == id:
            update = True
            task["description"] = description
            task["updatedAt"] = datetime.datetime.now().strftime("%c")
            print("Successfully update")
    if not update:
        print("Error")
        return
    save_tasks(tasks)


def delete_task(id):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == id:
            found = True
            break
    if not found:
        print("Error")
        return
    tasks = [task for task in tasks if task["id"] != id]
    save_tasks(tasks)


def main() -> None:
    add_task("Beli roti")
    add_task("Solat")
    update_task(1, "Beli roti dan susu")
    delete_task(99)


if __name__ == "__main__":
    main()
