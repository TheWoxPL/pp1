try:
    godziny=int(input("Podaj liczbę godzin: "))
    stawka=int(input("Podaj stawkę godzinową: "))
    wyplata=float()

    if godziny>40:
        wyplata=(40*stawka)+((godziny-40)*stawka*1.5)
    else:
        wyplata=stawka*godziny
    print(f"Wynagrodzenie: {wyplata}")
except:
    print("Błąd, podaj wartość numeryczną")