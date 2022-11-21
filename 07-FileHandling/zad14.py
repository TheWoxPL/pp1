file_name=input("Podaj nazwe pliku: ")
counter=0
with open(file_name) as file:
    for line in file:
        counter+=1

print("File name: ", file_name)
print("Number of lines: ", counter)