def compare(arr1, arr2):
    if len(arr1)==len(arr2):
        for i in range(0, len(arr1)):
            if arr1[i]!=arr2[i]:
                return False
    else:
        return False
    return True

arr1=["water","book","sky"]
arr2=["water","book","sky"]
print(f"Array1: {arr1}")
print(f"Array2: {arr2}")
print(f"Coomparison: ",compare(arr1, arr2))
arr1=[True,False]
arr2=[True,False,True]
print(f"Array1: {arr1}")
print(f"Array2: {arr2}")
print(f"Coomparison: ",compare(arr1, arr2))
arr1=[5,3,1]
arr2=[5,3,1]
print(f"Array1: {arr1}")
print(f"Array2: {arr2}")
print(f"Coomparison: ",compare(arr1, arr2))
arr1=[3,2,1]
arr2=[3,2]
print(f"Array1: {arr1}")
print(f"Array2: {arr2}")
print(f"Coomparison: ",compare(arr1, arr2))