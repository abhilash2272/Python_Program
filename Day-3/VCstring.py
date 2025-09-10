def vc(s):
    countV=0
    countC=0
    for i in s:
        if i.lower() in ('a','e','i','o','u'):
            countV+=1
        else:
            countC+=1
    print(f"Total number of vowels are {countV} and consonants are {countC}")
s=input("Enter String")
vc(s)
