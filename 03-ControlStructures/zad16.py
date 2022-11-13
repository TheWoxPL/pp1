try:
    num1=int(input("Podaj pierwszą liczbe:"))
    num2=int(input("Podaj drugą liczbe:"))
    if num1>num2:
        print(num2, num1)
    else: 
        print(num1, num2)
except:
    print("Podano wartość, która nie jest liczbą")