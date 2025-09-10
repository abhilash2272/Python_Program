def cou():
    ce=0
    co=0
    l=[]
    n=int(input("Enter :"))
    for i in range(n):
        l.append(int(input("Enter elements :")))
    for i in range(n):
        if(l[i]%2==0):
            ce=ce+1
        else:
            co=co+1
    print(f"total even numbers are {ce},total odd numbers are {co}")
cou()

    