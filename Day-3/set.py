def se():
    s=set()
    n=int(input("Enter the length"))
    for i in range(n):
        ele=input("Enter the element :")
        s=s | {ele}
    print(s)
se() 