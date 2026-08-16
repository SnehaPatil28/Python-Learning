
import time
tasks = []


def display_task():
    print("==== Task Manager ====")
    print("1. Add Task\n"
          "2. View Task\n"
          "3. Complete Task\n"
          "4. Delete Task\n"
          "0. Exit"
          )
    time.sleep(1)


def add_task():
    store_task = input("Enter the task: ")
    tasks.append({"title": store_task, "completed": False})
    print(f"Task {store_task} added successfully")

    time.sleep(1)


def view_task():
    print("====== My Tasks =====")

    if not tasks:
        print("No task found")

    for index, task in enumerate(tasks):
        status = "✔" if task["completed"] else " "
        print(f"{index + 1}. [{status}] {task["title"]}")

    print("=============================")
    time.sleep(1)


def complete_task():
    view_task()

    if not tasks:
        return

    try:
        task_number = int(input("Enter the task number: "))
        if task_number < 1 or task_number > len(tasks):
            print("Enter the valid number to mark as complete.")

        task_to_complete = tasks[task_number - 1]
        task_to_complete["completed"] = True
        print(f"Task '{task_to_complete["title"]}' marked as complete.")

    except ValueError:
        print("Please enter valid input!!!")

    time.sleep(1)


def delete_task():
    view_task()

    if not tasks:
        return

    try:
        task_num = int(input("Enter task number: "))
        if task_num < 1 or task_num > len(tasks):
            print("Enter valid number to delete task.")

        task_to_delete = tasks[task_num - 1]
        print(f"Task '{task_to_delete["title"]}' deleted successfully!!!")
        tasks.remove(task_to_delete)

    except ValueError:
        print("Please enter valid input!!!")

    time.sleep(1)


def main():
    while True:
        display_task()

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
            time.sleep(1)
        elif choice == '2':
            view_task()
            time.sleep(1)
        elif choice == '3':
            complete_task()
            time.sleep(1)
        elif choice == '4':
            delete_task()
            time.sleep(1)
        elif choice == '0':
            print("GoodByee!!")
            break
        else:
            print("Incorrect choice, choose between 0-4")


main()
