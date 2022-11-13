try:
    num1=float(input("Pierwsza liczba: "))
    num2=float(input("Druga liczba: "))
    if num1>0 or num2>0:
        print(f"One of {num1} {num2} is positive")
except:
    print("Nie podano liczby")