
import csv
with open("data.txt", "w",encoding="utf-8") as f1:
    f1.write("Hello\n")
    f1.write("Python\n")
with open("data.txt", "r", encoding="utf-8") as f1:
    lines = f1.readlines()

with open("data.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    for line in lines:
        writer.writerow([line.strip()])

#2
import csv
with open("file.txt", "w") as f:
    for i in range(1,11):
        f.write(str(i) + "\n")
with open("file.txt", "r") as f:
    numbers = f.readlines()

with open("file.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    for num in numbers:
        writer.writerow([num.strip()])

#3
import csv
with open("names.txt", "w", encoding="utf-8") as f1:
    name = input()
    names = name.split()
    for n in names:
        f1.write(n.title()+ "\n")

with open("names.txt", "r", encoding="utf-8") as f1:
    lines = f1.readlines()

with open("names.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name"])
    for line in lines:
        writer.writerow([line.strip().title()])



