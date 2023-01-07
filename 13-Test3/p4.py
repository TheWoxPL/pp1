def f(d):
    all=[]
    for i in d:
        if i[1]=="in":
            all.append(i[0])
        else:
            all.remove(i[0])
    all.sort()
    print(all)


cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]
f(cars)