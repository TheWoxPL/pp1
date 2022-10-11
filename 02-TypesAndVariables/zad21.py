from random import random

one=round((random()*100)%5+1)
user_guess=int(input("Try to guess dice roll(1-6): "))
if(one==user_guess):
    print("True")
else:
    print("False")
