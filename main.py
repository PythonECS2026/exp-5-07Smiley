# AIM: Task List Manager
# Coder:
# Date:
tasks = ["Sleep", "Getup", "Brush"]
print(f"Original Tasks: {tasks}")

# add task
tasks.append(input())
print(f"Tasks after Adding: {tasks}")

# edit task
edit_index = int(input())
tasks[edit_index] = input()
print(f"Tasks after Editing: {tasks}")

# remove task (IMPORTANT: expected index = 0)
remove_index = int(input())
tasks.pop(remove_index)
print(f"Tasks after Removing: {tasks}")

# sort tasks
tasks.sort()
print(f"Tasks after Sorting: {tasks}")
# add task

# add task (no prompt)

# Write your code here
# TODO: Add & Print new Task from user

# TODO: Edit & Print task selected by User

# TODO: Remove & Print a Task selected by User

# TODO: Sort & Print the Tasks






