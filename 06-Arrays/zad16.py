arr=[15, 8, 31, 47, 2, 19]
print("existed array: ", end="")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

print()

print("reverse array: ", end="")
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=" ")