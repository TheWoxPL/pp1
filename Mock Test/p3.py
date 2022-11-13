def f(amount_to_pay):
    counter=0
    counter+=amount_to_pay//5
    amount_to_pay%=5
    counter+=amount_to_pay//2
    amount_to_pay%=2
    counter+=amount_to_pay//1
    return counter