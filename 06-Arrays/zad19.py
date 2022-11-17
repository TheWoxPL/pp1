arr=[15, 8, 31, 47, 2, 19]
sum=0
i=0
while i<len(arr):
    print(arr[i], end=" ")
    sum+=arr[i]
    i+=1

print()
print(f"Arithmetic mean: {sum/len(arr)}")
