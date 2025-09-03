def num(n):
    if(n>0):
        print(f"{n} is an positive integer")
    elif(n<0):
        print(f"{n} is an negative integer")
    else:
        print(f"{n} is an zero")
n=int(input("Enter the number"))
num(n)