with open("countries.txt", "r", encoding="Utf-8") as file:
    with open("copylines.txt", "w", encoding="Utf-8") as copylines:
        for line in file:
            copylines.write(line)