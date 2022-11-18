import random as random

def rand_elem(array):
    return array[random.randint(0,len(array)-1)]
print(rand_elem([5,3,7,3]))

