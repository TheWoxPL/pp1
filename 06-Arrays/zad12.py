from traceback import print_tb


arr=[[2,5,4],[9,0,3]]
# a
print(arr)
#b 
print(f"Rows: {len(arr)}")
print(f"Columns: {len(arr[0])}")
#c
print(arr[0][1])
#c
print(arr[1][2])
#d
print(arr[1])
#f
for i in arr:
    for j in i:
        print(j, end=" ")
    print()
#g
for i in arr:
    print(i[len(i)-1])