def freh(s):
    max=s.count(s[0])
    for i in range(1,len(s)):
        max1=s.count(s[i])
        if(max<max1):
            max=max1
    print(max)
s=input("Enter string :")
freh(s)