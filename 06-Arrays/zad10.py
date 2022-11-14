from random import randint


arr=[]
for i in range(10):
    arr.append(randint(0,9))

print(arr)

i=0
odd=0
even=0
while i<len(arr)-1:
    if arr[i]%2==0:
        even+=arr[i]
    else:
        odd+=arr[i]
    i+=1

print(odd)
print(even)