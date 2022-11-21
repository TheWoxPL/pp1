file=open("shopping.txt", "a")
new_product=input("Next product: ")
file.write(new_product+"\n")
file.close()