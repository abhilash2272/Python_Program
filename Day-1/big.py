def greater(a,b,c):
    if a>b:
        if a>c:
            print(f"{a} is greater")
        else:
            print(f"{c} is greater")
    else:
        print(f"{b} is greater")
a=int(input(" Enter a number"))
b=int(input(" Enter a number"))
c=int(input(" Enter a number"))
greater(a,b,c)