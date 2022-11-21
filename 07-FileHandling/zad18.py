with open("MeatAndFIsh.txt") as file1:
    with open("GrainsAndBread.txt") as file2:
        with open("shoppinglist.txt", "w") as file3:
            for line in file1:
                file3.write(line)
            for line in file2:
                file3.write(line)   