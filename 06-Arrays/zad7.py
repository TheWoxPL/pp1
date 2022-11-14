array=[1,2,3,4,5]
#a
array[0]=array[0]-1
print(array)
#b
array[len(array)-1]=array[len(array)-1]*4
print(array)
#c
array[int(len(array)/2)]=array[int(len(array)/2)]*2
print(array)
#d
i=0
while i<len(array):
    array[i]+=3
    i+=1
print(array)