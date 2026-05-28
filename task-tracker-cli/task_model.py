import datetime


def create_task(id, description) -> dict:
    clock = datetime.datetime.now()
    task = {
        "id": id,
        "description": description,
        "status": "todo",
        "createdAt": clock.strftime("%c"),
        "updatedAt": clock.strftime("%c")
    }
    return task


def main() -> None:
    task = create_task(1, "Test Task")
    print(task)


if __name__ == "__main__":
    main()
