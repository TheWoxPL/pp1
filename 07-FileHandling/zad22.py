import csv
with open('students.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    for row in reader:
        if int(row[2])<30:
            print(f"{row[0]}\t{row[1]}\t{row[4]}")