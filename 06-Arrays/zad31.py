arr=[4,2,1,5,6,2,6,8,3]
arr_even=[]
arr_odd=[]
for i in arr:
    if i%2==0:
        arr_even.append(i)
    else:
        arr_odd.append(i)

print(arr_even, arr_odd)