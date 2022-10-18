pin="0805"
i=0
while True:
    i+=1
    if str(input("Enter the PIN code: "))==pin:
        print("PIN is correct")
        break
    else:
        print("Incorrect...")
    if i==3:
        print("Sorry, your payment card has been blocked.")
        break