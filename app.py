from utils import add_entry, read_entries

add_entry("Project initialized by A")

for line in read_entries():
    print(line)
    
add_entry("B: first change")

add_entry("A: second change")

add_entry("B: updating logic")

add_entry("A: refining update")


def delete_last_entry():
    with open("data.txt", "r") as f:
        lines = f.readlines()
    with open("data.txt", "w") as f:
        f.writelines(lines[:-1])

delete_last_entry()
add_entry("B: replaced deleted entry")