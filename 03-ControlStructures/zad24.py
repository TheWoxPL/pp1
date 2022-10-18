x=5
i=1
while i<=x:
    for j in range(0, i):
        print("*", end=" ")
    print()
    i+=1

i=x-1
x=1
while i>=x:
    for j in range(0, i):
        print("*", end=" ")
    print()
    i-=1
    