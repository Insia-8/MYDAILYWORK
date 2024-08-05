
tasks = []

def add_task(description, due_date=None, priority='medium'):
    task = {
        'description': description,
        'due_date': due_date,
        'priority': priority,
        'completed': False}
    tasks.append(task)


def format_task(task, index):
    if task['completed']:
        status = 'Done'
    else:
        status = 'Pending'
    if task['due_date']:
        due_date = task['due_date']
    else:
        due_date = "No due date"
    return f"{index + 1}. [{status}] {task['description']} (Due: {due_date}, Priority: {task['priority']})"


def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            print(format_task(task, i))


def update_task(index, description=None, due_date=None, priority=None, completed=None):
    if 0 <= index < len(tasks):
        if description:
            tasks[index]['description'] = description
        if due_date:
            tasks[index]['due_date'] = due_date
        if priority:
            tasks[index]['priority'] = priority
        if completed is not None:
            tasks[index]['completed'] = completed
    else:
        print("Invalid task number.")


def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    else:
        print("Invalid task number.")


def main():
    while True:
        print("\nTo-Do List")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD) or leave empty: ")
            priority = input("Enter priority (low, medium, high): ")
            add_task(description, due_date if due_date else None, priority)
        elif choice == '3':
            index = int(input("Enter task number to update: ")) - 1
            description = input("Enter new description or leave empty: ")
            due_date = input("Enter new due date (YYYY-MM-DD) or leave empty: ")
            priority = input("Enter new priority (low, medium, high) or leave empty: ")
            completed = input("Is the task completed? (yes/no): ")

            if description:
                update_task(index, description=description)
            if due_date:
                update_task(index, due_date=due_date)
            if priority:
                update_task(index, priority=priority)
            update_task(index, completed=completed)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == '5':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

