def sum_of_digits(number):
    sum=0
    for i in str(number):
        sum+=int(i)
    print(f"Sum of digits in {number} is {sum}")

sum_of_digits(7182)