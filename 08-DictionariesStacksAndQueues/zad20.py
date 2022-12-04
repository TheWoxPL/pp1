import stack
natural_number=16
x=natural_number
while x>0:
    stack.push(x%2)
    x//=2

print(f"Natural number: {natural_number}")
print(f"Ninary number: ", end="")
for i in range(len(stack.stack)):
    print(stack.pop(), end="")