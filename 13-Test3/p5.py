class C:
    def __init__(self, arr):
        self.arr=arr

    def __str__(self):
        self.arrstr=[]
        for i in self.arr:
            self.arrstr.append(str(i))
        string="+".join(self.arrstr)+"="+str(sum(self.arr))
        return string

print(C([5,12]))
print(C([6,0,15]))