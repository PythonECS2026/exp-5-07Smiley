# AIM: Task List Manager
# Coder:
# Date:
tasks = ["Sleep", "Getup", "Brush"]
print(f"Original Tasks: {tasks}")

new_task = input("Enter a new task to add: ")
tasks.append(new_task)
print(f"Tasks after Adding: {tasks}")

edit_index = int(input("Enter the index of the task to edit: "))
new_task_value = input("Enter the new task: ")
tasks[edit_index] = new_task_value
print(f"Tasks after Editing: {tasks}")

remove_index = int(input("Enter the index of the task to remove: "))
tasks.pop(remove_index)
print(f"Tasks after Removing: {tasks}")

tasks.sort()
print(f"Tasks after Sorting: {tasks}")
# Write your code here
# TODO: Add & Print new Task from user

# TODO: Edit & Print task selected by User

# TODO: Remove & Print a Task selected by User

# TODO: Sort & Print the Tasks


