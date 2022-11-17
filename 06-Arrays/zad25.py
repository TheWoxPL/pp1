def occurs(number, array):
    for i in array:
        if i==number:
            return True
    return False

number_from_keyboard=int(input("Number: "))
print("Array: [15, 38, 7, 23, 14]3")
if occurs(number_from_keyboard, [15, 38, 7, 23, 14]):
    print(f"Result: number {number_from_keyboard} appears in the array")
else:
    print("Result: this number doesn't appear in array")