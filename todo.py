def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")

def list_tasks():
    with open("tasks.txt", "r") as f:
        return f.readlines()