arr=[
    [9,0,0],
    [9,1,1],
    [9,2,2],
    [9,3,3],
    [9,4,4]
]
print(arr)

for i in range(0, len(arr)):
    tmp=arr[i][0]
    arr[i][0]=arr[i][len(arr[i])-1]
    arr[i][len(arr[i])-1]=tmp

print(arr)