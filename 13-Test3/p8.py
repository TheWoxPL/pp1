class C:
    def __init__(self, dict):
        self.dict=dict
        
    def m(self, n):
        self.list=[]
        for i in self.dict:
            sum=0
            for grade in self.dict[i]:
                sum+=grade
            if sum/len(self.dict[i])>=n:
                self.list.append(i)
        self.list.sort()
        print(",".join(self.list))


s = C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})
s.m(5)