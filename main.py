import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()


while True:
    print("\n===== STUDENT TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append({
            "task": task,
            "completed": False
        })
        save_tasks(tasks)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for number, item in enumerate(tasks, start=1):
                status = "✓" if item["completed"] else "○"
                print(f"{number}. {status} {item['task']}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for number, item in enumerate(tasks, start=1):
                print(f"{number}. {item['task']}")

            task_number = int(input("Enter task number to complete: "))

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                save_tasks(tasks)
                print("Task completed!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for number, item in enumerate(tasks, start=1):
                print(f"{number}. {item['task']}")

            task_number = int(input("Enter task number to delete: "))

            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                save_tasks(tasks)
                print(f"Deleted: {deleted_task['task']}")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")