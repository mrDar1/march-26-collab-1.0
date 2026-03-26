from todo import add_task, list_tasks

add_task("Initial task by A")

tasks = list_tasks()
for t in tasks:
    print(t)
    
add_task("B: buy groceries")
add_task("A: clean room")

def remove_last_task():
    with open("tasks.txt", "r") as f:
        lines = f.readlines()
    with open("tasks.txt", "w") as f:
        f.writelines(lines[:-1])
        
remove_last_task()
add_task("B: replaced last task")

#!שים לב לפונקציה
def update_first_task(new_task):
    with open("tasks.txt", "r") as f:
        lines = f.readlines()
    lines[0] = new_task + "\n"
    with open("tasks.txt", "w") as f:
        f.writelines(lines)