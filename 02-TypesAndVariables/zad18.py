import math
a=int(input("Podaj a: "))
b=int(input("Podaj b: "))
c=int(input("Podaj c: "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)
