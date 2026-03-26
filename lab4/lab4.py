num_tasks = int(input("Enter number of tasks: "))
tasks = {}

for i in range(num_tasks):
    task_name = input("Enter task name: ")
    num_deps = int(input(f"How many dependencies for {task_name}? "))

    dependencies = []

    for j in range(num_deps):
        dep = input(f"Enter dependency {j + 1}: ")
        dependencies.append(dep)

    tasks[task_name] = dependencies


print("\nTASK STRUCTURE:")
for task, deps in tasks.items():
    print(f"{task} -> {deps}")


print("\nINITIAL TASKS (no dependencies):")
found_initial = False
for task, deps in tasks.items():
    if len(deps) == 0:
        print(task)
        found_initial = True

if not found_initial:
    print("None")  #


completed_tasks = set()
execution_order = []

print("\nEXECUTION ORDER:")


while len(execution_order) < len(tasks):
    task_processed_in_this_round = False

    for task, deps in tasks.items():
        if task in completed_tasks:
            continue


        all_done = True
        for d in deps:
            if d not in completed_tasks:
                all_done = False
                break

        if all_done:
            completed_tasks.add(task)
            execution_order.append(task)
            print(f"Step {len(execution_order)}: {task}")
            task_processed_in_this_round = True

            break


    if not task_processed_in_this_round:
        break


if len(completed_tasks) == len(tasks):
    print("\nALL TASKS COMPLETED SUCCESSFULLY")
else:
    print("\nNo task can be started.")
    print("ERROR: Circular dependency detected!")
    print("These tasks could not be completed:")
    for task in tasks:
        if task not in completed_tasks:
            print(task)
