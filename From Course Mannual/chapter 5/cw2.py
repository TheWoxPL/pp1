maksimum=0
minimum=0
once=True

while True:
    try:
        liczba=input("Wprowadź liczbę: ")
        if once:
            once=not once
            maksimum=int(liczba)
            minimum=int(liczba)
        if int(liczba)>maksimum:
            maksimum=int(liczba)
        if int(liczba)<minimum:
            minimum=int(liczba)
        
    except:
        if liczba=="gotowe":
            print(maksimum, minimum)
            break
        else:
            print("Nieprawidłowe wejście")