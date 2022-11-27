import re
with open("zad15.txt", "r") as file:
    found=re.findall("\w{6,}", file.read())
    for i in found:
        print(i, end="\n")