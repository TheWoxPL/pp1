with open("countries.txt", "r", encoding="Utf-8") as file:
    with open("copy.txt", "w", encoding="Utf-8") as copy:
        copy.write(file.read())