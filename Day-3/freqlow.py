def frel(s):
    min=s.count(s[0])
    for i in range(1,len(s)):
        min1=s.count(s[i])
        if(min>min1):
            min=min1
    print(min)
s=input("Enter string :")
frel(s)