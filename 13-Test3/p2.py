def f(arr):
    counter=1
    if len(arr)==len(arr[0]):
        for i in range(0, len(arr)):
            for j in range(0, len(arr[0])):
                if arr[i][j]!=arr[0][j]*counter:
                    return False
            counter+=1
        return True
    return False

print(f([[1,2,3],[2,4,6],[3,6,9]]))
print(f([[1,2],[3,6]]))
print(f([[1,2,3],[2,4,6]]))
print(f([[1,2,3],[2,5,6]]))