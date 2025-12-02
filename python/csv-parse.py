#Given a CSV file of users, print users with inactive status.
# id,name,status
# 1,Alice,active
# 2,Bob,inactive
# 3,Jane,active

import csv


with open("file.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["status"] == "inactive":
            print(row["name"])