def create_2d_arr(x,y):
    arr=[]
    for i in range(0,y):
        tmp_arr=[]
        for j in range(0,x):
            tmp_arr.append(0)
        arr.append(tmp_arr)

    return arr

print(create_2d_arr(3,6))

