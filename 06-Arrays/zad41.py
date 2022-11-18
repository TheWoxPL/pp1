arr=[
    [0,0,0],
    [1,1,1],
    [2,2,2],
    [3,3,3],
    [4,4,4]
]
print(arr)

tmp=arr[0]
arr[0]=arr[len(arr)-1]
arr[len(arr)-1]=tmp

print(arr)