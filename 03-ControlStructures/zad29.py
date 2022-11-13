quantity=0
sum=0
while True:
    entered_number=int(input("Enter number: "))
    if entered_number==0:
        break
    quantity+=1
    sum+=entered_number

print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean={sum/quantity}")