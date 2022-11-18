def arr_convert(arr):
    arr_1d=[]
    for i in arr:
        for j in i:
            arr_1d.append(j)
    return arr_1d

arr1=[[2,3],[1,5]]
arr2=[[5,0,3,7,5],[9,0,9,1,2]]
arr3=[[2,1],[3,5],[7,4],[2,6]]


print(arr_convert(arr1))
print(arr_convert(arr2))
print(arr_convert(arr3))
