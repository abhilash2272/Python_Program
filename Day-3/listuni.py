def uni():
    l = []
    n = int(input("Enter length of list: "))
    for i in range(n):
        l.append(int(input("Enter element: ")))
    for i in range(n):
        if(l[i] not in l[:i]):
            print(l[i])
uni()