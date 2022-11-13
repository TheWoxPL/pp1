suma=0
licznik=0
while True:
    try:
        liczba=input("Wprowadź liczbę: ")
        suma+=int(liczba)
        licznik+=1
    except:
        if liczba=="gotowe":
            print(suma, licznik, suma/licznik)
            break
        else:
            print("Nieprawidłowe wejście")