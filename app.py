from utils import add_entry, read_entries

add_entry("Project initialized by A")

for line in read_entries():
    print(line)
    
add_entry("B: first change")

add_entry("A: second change")