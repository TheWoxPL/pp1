with open("zad15.txt", "r") as file:
    i=0
    for line in file:
        if i==5:
            input("Prees enter...")
            i=0
        i+=1
        print(line)