def fre(s):
    for i in range(len(s)):
        k=s.count(s[i])
        if s[i] not in s[:i]:
            print(f"{s[i]}{k}",end="")
s=input("Enter string :")
fre(s)