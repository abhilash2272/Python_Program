def len():
    s=input("Enter string :")
    s1=input('Enter String :')
    count=0
    for i in s:
        count+=1
    print(f"Length of the string {s} is {count}")
    print(s+s1,"concatenate string")
    if s==s1:
        print("Equal")
    else:
        print("Not same")
len()