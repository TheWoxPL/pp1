array=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
the_longest_name=""
for i in array:
    if len(the_longest_name)<len(i):
        the_longest_name=i

print(f"The longest name: {the_longest_name}")