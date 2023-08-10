def show_menu():
    print("Command-line To-Do List")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print()


def view_todo_list(todo_list):
    if not todo_list:
        print("Your To-Do list is empty.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")
    print()


def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully.")
    print()


def update_task(todo_list):
    view_todo_list(todo_list)
    task_number = int(input("Enter the task number to update: "))
    if 1 <= task_number <= len(todo_list):
        updated_task = input("Enter the updated task: ")
        todo_list[task_number - 1] = updated_task
        print("Task updated successfully.")
    else:
        print("Invalid task number.")
    print()


def delete_task(todo_list):
    view_todo_list(todo_list)
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(todo_list):
        del todo_list[task_number - 1]
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")
    print()


def main():
    todo_list = []
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            update_task(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        print()


if __name__ == "__main__":
    main()
