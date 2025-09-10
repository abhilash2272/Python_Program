def listneg(n):
    l=[]
    for i in range(n):
        l.append(int(input("Enter elements :")))
    for i in range(n):
        if(l[i]<0):
            print(l[i])
n=int(input("Enter length of list :"))
listneg(n)