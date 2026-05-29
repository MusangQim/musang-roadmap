from json_handler import load_tasks
from task_operations import save_tasks
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
    save_tasks(tasks)


def list_tasks(filter=None):
    tasks = load_tasks()
    if filter == None:
        print(tasks)
    else:
        for task in tasks:
            if task["status"] == filter:
                print(task)
            
def main() -> None:
    
if __name__ == "__main__":
    main()