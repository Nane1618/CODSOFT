def add(tasks, new_task):
    tasks.append(new_task)
    print(f"Task '{new_task}' added successfully")

def remove(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed = tasks.pop(task_index - 1)
        print(f"Task '{removed}' removed successfully")
    else:
        print("Invalid task index")

def display(tasks):
    if not tasks:
        print("No tasks to display")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
def main():
    tasks = []
    while True:
        print("\n1.DISPLAY TASKS ")
        print("2. ADD TASK")
        print("3. REMOVE TASK")
        print("4. EXIT")

        choice = input("Enter your choice: ")

        if choice == "1":
            display(tasks)
        elif choice == "2":
            new_task = input("Enter the new task: ")
            add(tasks, new_task)
        elif choice == "3":
            display(tasks)
            task_index = int(input("Enter the task number to remove: "))
            remove(tasks, task_index)
        elif choice == "4":
            print("Ending of List")
            break
        else:
            print("Invalid choice. Please enter a number between 1 to 4")

if __name__ == "__main__":
    main()
