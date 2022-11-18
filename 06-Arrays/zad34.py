arr1=[4,2,1]
arr2=[4,2,5,2,66]

counter=0
for i in arr1:
    for j in arr2:
        if i==j:
            counter+=1
            break

if counter==len(arr1):
    print("This arr is substract")
else:
    print("This array is not substract")