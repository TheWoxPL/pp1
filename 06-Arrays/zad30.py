def minmax(array):
    array.sort()
    return [array[0], array[-1]]

print(minmax([4,2,5,1,7]))