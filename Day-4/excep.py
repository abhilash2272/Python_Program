def exp():
    x=int(input("Enter the number :"))
    y=int(input("Enter the number :"))
    try:
        print(x/y)
    except:
        print("Division by zero is not allowed")
exp()    