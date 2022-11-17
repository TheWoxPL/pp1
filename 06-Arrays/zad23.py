def bubblesort(array):
    for i in range(0, len(array)):
        for j in range(i, len(array)):
            if array[j]<array[i]:
                tmp=array[i]
                array[i]=array[j]
                array[j]=tmp
    return(array)

print(bubblesort([12,5,1,65,7,4,2,6,8,45,32,45,5]))
print(bubblesort([4,2,5,5,132,55,15,565,57,34,2,6,8,45,32,45,5]))
print(bubblesort([125,55,1,655,7,45,2,6,85,45,323,435,5]))