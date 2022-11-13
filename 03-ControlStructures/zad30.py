N=5
number=2
while N>0:
    if_prime=True
    for i in range(2, number):
        if number%i==0:
            if_prime=False
    if if_prime:
        print(number, end=" ")
        N-=1
    number+=1