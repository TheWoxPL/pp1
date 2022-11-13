def f(number, even):
    number=str(number)
    sum=0
    mod=1
    if even:
        mod=0
    
    for digit in number:
        if int(digit)%2==mod:
            sum+=int(digit)
    
    return sum