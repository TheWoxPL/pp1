def indentity_matrix(n):
    arr=[]
    for i in range(0, n):
        tmp=[]
        for j in range(0, n):
            if j==i:
                tmp.append(1)
            else:
                tmp.append(0)
        arr.append(tmp)
    return arr

def display_arr_2d(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
    print()

display_arr_2d(indentity_matrix(3))
display_arr_2d(indentity_matrix(5))
display_arr_2d(indentity_matrix(8))
