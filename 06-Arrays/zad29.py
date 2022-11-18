arr=[5,2,6,6,2,3,7,3]
arr.sort()
number=int(input("Number: "))
for i in arr:
    if i>number:
        print(i, end=" ")