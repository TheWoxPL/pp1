a=4
b=15

for i in range(0, a):
    if i==0 or i==a-1:
        for j in range(0, b):
            print("*", end="")
    else:
        for j in range(0, b):
            if j==0 or j==b-1:
                print("*", end="")
            else:
                print(" ", end="")
    print(" ")