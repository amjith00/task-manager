import json
import os

TASKS_FILE = 'tasks.json'


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)


def display_tasks(tasks):
    print("\nYour Tasks:")
    if not tasks:
        print("No tasks to display.")
        return
    for i, task in enumerate(tasks, start=1):
        status = '✅' if task['completed'] else '❌'
        print(f"{i}. {task['title']} [{status}]")


def add_task(tasks):
    title = input(" Enter task title: ")  # INPUT HERE
    tasks.append({'title': title, 'completed': False})
    print(f"Task '{title}' added.")


def complete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input(" Enter task number to mark as complete: ")) - 1  # INPUT HERE
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            print(f"Task '{tasks[index]['title']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1  # INPUT HERE
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f" Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def menu():
    tasks = load_tasks()

    while True:
        print("\n---  Task Manager ---")
        print("1. View tasks")
        print("2.  Add task")
        print("3.  Mark task as complete")
        print("4. Delete task")
        print("5.  Save & Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("✅ Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == '__main__':
    menu()

