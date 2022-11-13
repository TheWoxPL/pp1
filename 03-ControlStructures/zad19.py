dog_age_in_human=float(input("Enter the dog's age in human years: "))
dog_age_in_dog_age=0
if dog_age_in_human>=2:
    dog_age_in_dog_age+=2*10.5+(dog_age_in_human-2)*4
else:
    dog_age_in_dog_age=dog_age_in_human*10.5

print(f"The dog's age in dog’s years is {int(dog_age_in_dog_age)} years.")