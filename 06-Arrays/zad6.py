array=[2,3,7,5,4]
# a
print(array)
#b
print(len(array))
#c
print(array[0])
#d
print(array[1])
#e
print(array[len(array)-1])
#f
print(array[len(array)-2])
#g
print(array[0]+array[len(array)-1])
#h
print(array[int(len(array)/2)])
#i
i=0
while i<len(array):
    if i==len(array)-1:
        print(array[i], end="")
    else:
        print(array[i], end=", ")
    i+=1
#j
print()
i=0
while i<=int(len(array)/2):
    print(array[i], end=" ")
    i+=1
