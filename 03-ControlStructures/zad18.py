amount=int(input("Enter the amount in PLN: "))
five=amount//5
amount-=five*5
two=amount//2
amount-=two*2
one=amount//1
print(f"The amount of PLN {five*5+two*2+one} in coins: ")
print(f"5 zł - {five}")
print(f"2 zł - {two}")
print(f"1 zł - {one}")
    