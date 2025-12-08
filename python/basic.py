# File handleing
with open("file.txt") as f:
    for line in f:
        print(line)
        
# Dictionaries
d = {"a":1}
d["b"] = 2
for k, v in d.items():
    print(f"Key={k}, Value={v}")

#List Comprehension
values = []
filtered = [x for x in values if "error" in x]

# Sort function = creates new list
sorted_values = sorted(values)
# Sort method = modifies current list
values.sort()

# Dedupe
unique = set(values)

#datetime
from datetime import datetime
dt = datetime.strptime("2025-09-17 04:20:00", "%Y-%m-%d %H:%M:%S")

#Regex
import re
m = re.search(r"level=(\w+)", line)
if m:
    print(m.group(1))
    
