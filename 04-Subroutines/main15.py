import mymath

computer_number=mymath.generate_number()

while True:
    user_number=mymath.read_number()

    if user_number==computer_number:
        print("You won!")
        break
    print("Try again :(")