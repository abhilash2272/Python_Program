def perfect(n):
    for i in range(1,n):
        if n%i==0:
            print(f"{i}",end=" ")
n=int(input("Enter number: "))
perfect(n)

