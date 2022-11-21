film_titles=["Shrek","Auta","James Bond","Elvis 2022","Minionki"]
file=open("zad11.txt","w")
for film in film_titles:
    file.write(film+"\n")
file.close()