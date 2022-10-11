height=int(input("Wzrost w cm: "))
from math import ceil, floor
cm=height
feet=int(height/2.54//12)
inches=ceil(height/2.54-12*feet)
print(f"I am {height} tall, i.e. {feet} feet and {inches} inches.")