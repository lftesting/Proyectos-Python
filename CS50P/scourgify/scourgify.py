import csv
import sys

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)


with open(sys.argv[1]) as file:
    students = []
    try:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].strip().split(",")
            last = last.strip()
            first = first.strip()
            students.append({"first": first,"last": last, "house":row["house"]})

    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w") as new_file:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(new_file, fieldnames= fieldnames)
    writer.writeheader()
    for student in students:
        writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})




