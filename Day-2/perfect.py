def perfect(n):
    for i in range(1,n+1):
        sum=0
        for j in range(1,i):
            if i%j==0:
                sum+=j
        if(i==sum):
            print(f"{i} is a perfect number")
n=int(input("Enter number: "))
perfect(n)

