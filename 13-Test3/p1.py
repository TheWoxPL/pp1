def f(n):
    str=""
    if n>=0:
        for i in range(n):
            if i%5==0  and i>0:
                str+="-"
            str+="/"

    return str

def main():
    print(f(-4))
    print(f(15))
    print(f(16))

if __name__=="__main__":
    main()