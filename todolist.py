tasks = []

number_of_tasks = int(input("How many tasks do you want to add?" ))

for i in range(number_of_tasks):
    task = input(f"Enter task {i + 1}: ")
    tasks.append(task)

print("\nYour To-Do List: ")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")