def digit(n):
    count=0
    while(n>0):
        r=n%10
        count+=1
        n=n//10
    print(count)
n=int(input("Enter number"))
digit(n)
