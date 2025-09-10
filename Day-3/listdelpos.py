def delpos():
    l=[]
    n=int(input("Enter :"))
    for i in range(n):
        l.append(int(input("Enter elements :")))
    p=int(input("Enter index to delete :"))
    l.pop(p)
    print(l)
delpos()