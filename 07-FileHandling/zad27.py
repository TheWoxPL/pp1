import re
with open("grades.txt", "r") as file:
    found=re.findall("[0-9].[0-9]", file.read())
    sum=0
    for i in found:
        sum+=float(i)

    print(f"Arithemtic mean of student's grades: {round(sum/len(found), 1)}")