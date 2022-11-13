from random import random


def read_number():
    return int(input("Enter a number: "))

def generate_number():
    return int(random()*100%10)