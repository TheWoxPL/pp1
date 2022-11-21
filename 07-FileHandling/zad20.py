import random as random

with open("randomintegers.txt", "w") as file:
    for i in range(50):
        file.write(str(random.randint(100,999))+"\n")