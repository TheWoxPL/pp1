arr=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        if i==j:
            arr[i][j]=1

for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        print(arr[i][j], end=" ")
    print()