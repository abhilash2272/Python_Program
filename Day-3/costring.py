def fre(s):
    countA=0
    countD=0
    countSC=0
    for i in s:
        if i.isalpha():
            countA+=1
        elif i.isdigit():
            countD+=1
        else:
            countSC+=1
    print(f"Total number of digits are {countD},alphabets are{countA},specialcharacters are {countSC}")
s=input("Enter string :")
fre(s)