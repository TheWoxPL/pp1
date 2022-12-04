import stack

def rpn(str):
    for i in str:
        if i=="+":
            stack.push(stack.pop()+stack.pop())
        elif i=="-":
            stack.push(stack.pop()-stack.pop())
        elif i=="*":
            stack.push(stack.pop()*stack.pop())
        elif i=="/":
            stack.push(1/stack.pop()*stack.pop())
        elif i>="0" and i<="9":
            stack.push(int(i))
        elif i=="=":
            return stack.pop()
            
print(rpn("23+="))
print(rpn("241+*="))
print(rpn("23+45+*="))
print(rpn("831+/32-4+*="))