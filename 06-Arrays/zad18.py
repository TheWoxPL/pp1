arr=[15, 8, 31, 47, 2, 19]
sum=0
for i in arr:
    print(i, end=" ")
    sum+=i

print()
print(f"Arithmetic mean: {sum/len(arr)}")
