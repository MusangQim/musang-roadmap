import json
import os


def load_tasks() -> list:
    if not os.path.exists("tasks.json"):
        with open("tasks.json", 'w') as file:
            file.write("[]")
        with open("tasks.json", 'r') as files:
            content = json.load(files)
    return (content)


def main() -> None:
    tasks = load_tasks()
    print(tasks)


if __name__ == "__main__":
    main()
