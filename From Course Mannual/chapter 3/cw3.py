try:
    liczba=float(input("Podaj wartość: "))
    if liczba>=0.9:
        ocena="5,0"
    elif liczba>=0.8:
        ocena="4,5"
    elif liczba>=0.7:
        ocena="4,0"
    elif liczba>=0.6:
        ocena="3,5"
    elif liczba>=0.5:
        ocena="3,0"
    elif liczba<0.5:
        ocena="2,0"
    print(ocena)

except:
    print("Niepoprawna wartość")