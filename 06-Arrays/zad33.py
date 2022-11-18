arr=[5,2,9,44,37,9]
for i in range(0, len(arr)):
    if arr[i]<10:
        arr[i]="   "+str(arr[i])
    elif arr[i]>=10 and arr[i]<100:
        arr[i]="  "+str(arr[i])
    elif arr[i]>=100 and arr[i]<1000:
        arr[i]=" "+str(arr[i])

print("|", end="")
for i in arr:
    print(i, end="|")
