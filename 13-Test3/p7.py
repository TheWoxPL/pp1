class C:
    @staticmethod
    def m1(number):
        new_number=""
        for i in str(number):
            if int(i)%2==0:
                new_number+=i
        print(new_number)

    @staticmethod
    def m2(n):
        for i in range(0, len(str(n))-1):
            if int(str(n)[i])>int(str(n)[i+1]):
                return False
        return True

C.m1(4231564)
print(C.m2(125579))
print(C.m2(4557879))