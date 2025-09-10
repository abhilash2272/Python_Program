def max2():
    l=[]
    n=int(input("Enter length :"))
    for i in range(n):
        l.append(int(input("Enter elements :")))
    l.sort()
    print("Second largest element is :",l[n-2])
max2()
