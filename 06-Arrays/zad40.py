arr=[[-38, 19], 
    [5,40],
    [-7,111],
    [29,161]]

max=[arr[0][0],0,0]
min=[arr[0][0],0,0]

for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        if arr[i][j]>max[0]:
            max[0]=arr[i][j] #the value
            max[1]=j #row
            max[2]=i #col

        if arr[i][j]<min[0]:
            max[0]=arr[i][j] #the value
            max[1]=j #row
            max[2]=i #col

print(max)
print(min)