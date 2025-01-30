import json
import os
import datetime

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, description, deadline, priority):
        task = {'description': description, 'deadline': deadline, 'status': 'pending', 'priority': priority}
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task['description']} - {task['deadline']} - {task['status']} - {task['priority']}")

    def update_task(self, task_number, description=None, deadline=None, status=None, priority=None):
        try:
            task = self.tasks[task_number - 1]
            if description:
                task['description'] = description
            if deadline:
                task['deadline'] = deadline
            if status:
                task['status'] = status
            if priority:
                task['priority'] = priority
            self.save_tasks()
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
            self.save_tasks()
        except IndexError:
            print("Invalid task number.")

    def search_tasks(self, keyword):
        found_tasks = [task for task in self.tasks if keyword.lower() in task['description'].lower()]
        if found_tasks:
            for i, task in enumerate(found_tasks, 1):
                print(f"{i}. {task['description']} - {task['deadline']} - {task['status']} - {task['priority']}")
        else:
            print("No tasks found.")

    def sort_tasks(self, attribute):
        if attribute == 'deadline':
            self.tasks.sort(key=lambda x: datetime.datetime.strptime(x['deadline'], '%Y-%m-%d'))
        elif attribute == 'status':
            self.tasks.sort(key=lambda x: x['status'])
        self.save_tasks()

    def check_due_date(self):
        today = datetime.datetime.today()
        for task in self.tasks:
            deadline = datetime.datetime.strptime(task['deadline'], '%Y-%m-%d')
            if (deadline - today).days <= 1:
                print(f"Task '{task['description']}' is due soon.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management Application")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Update a Task")
        print("4. Delete a Task")
        print("5. Search Tasks")
        print("6. Sort Tasks")
        print("7. Check Due Date")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            deadline = input("Enter task deadline (YYYY-MM-DD): ")
            priority = input("Enter task priority (high/medium/low): ")
            task_manager.add_task(description, deadline, priority)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number: "))
            description = input("Enter new description (press Enter to skip): ")
            deadline = input("Enter new deadline (press Enter to skip): ")
            status = input("Enter new status (pending/completed) (press Enter to skip): ")
            priority = input("Enter new priority (high/medium/low) (press Enter to skip): ")
            task_manager.update_task(task_number, description or None, deadline or None, status or None, priority or None)
        elif choice == '4':
            task_number = int(input("Enter task number: "))
            task_manager.delete_task(task_number)
        elif choice == '5':
            keyword = input("Enter search keyword: ")
            task_manager.search_tasks(keyword)
        elif choice == '6':
            attribute = input("Enter attribute to sort by (deadline/status): ")
            task_manager.sort_tasks(attribute)
        elif choice == '7':
            task_manager.check_due_date()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

