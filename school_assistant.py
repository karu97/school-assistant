import datetime

class SchoolAssistant:
    def __init__(self):
        self.todo_list = []
        self.timetable = {}
        self.reminders = {}

    def add_task(self, task):
        self.todo_list.append(task)
        print(f"Task '{task}' added to your to-do list.")

    def view_tasks(self):
        if not self.todo_list:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.todo_list, 1):
                print(f"{i}. {task}")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.todo_list):
            removed_task = self.todo_list.pop(task_number - 1)
            print(f"Task '{removed_task}' removed from your to-do list.")
        else:
            print("Invalid task number.")

    def add_class(self, day, time, subject):
        if day not in self.timetable:
            self.timetable[day] = []
        self.timetable[day].append((time, subject))
        print(f"Class '{subject}' at '{time}' added to your timetable on {day}.")

    def view_timetable(self):
        if not self.timetable:
            print("Your timetable is empty.")
        else:
            print("Timetable:")
            for day, classes in self.timetable.items():
                print(f"{day}:")
                for time, subject in classes:
                    print(f"  {time} - {subject}")

    def set_reminder(self, date, reminder):
        self.reminders[date] = reminder
        print(f"Reminder set for {date}: '{reminder}'.")

    def view_reminders(self):
        if not self.reminders:
            print("You have no reminders set.")
        else:
            print("Reminders:")
            for date, reminder in self.reminders.items():
                print(f"{date}: {reminder}")

    def calculate(self, expression):
        try:
            result = eval(expression)
            print(f"The result of '{expression}' is: {result}")
        except Exception as e:
            print(f"Error: {e}")
            

# Example Usage
assistant = SchoolAssistant()

# Add tasks
assistant.add_task("Math homework")
assistant.add_task("Science project")

# View tasks
assistant.view_tasks()

# Remove a task
assistant.remove_task(1)

# View tasks again
assistant.view_tasks()

# Add classes
assistant.add_class("Monday", "09:00 AM", "Math")
assistant.add_class("Monday", "10:00 AM", "English")
assistant.add_class("Tuesday", "11:00 AM", "Science")

# View timetable
assistant.view_timetable()

# Set reminders
assistant.set_reminder("2024-07-10", "Science project due")
assistant.set_reminder("2024-07-15", "Math exam")

# View reminders
assistant.view_reminders()

# Perform calculations
assistant.calculate("5 + 3 * 2")
assistant.calculate("10 / 2")
