def median(array):
    for i in range(0, len(array)):
        for j in range(i, len(array)):
            if array[j]<array[i]:
                tmp=array[i]
                array[i]=array[j]
                array[j]=tmp
    return array[len(array)//2]

print(median([1,0,9,4,6]))
print(median([6,8,3,1,0,5,7]))