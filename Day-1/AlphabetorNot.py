def alphabet(ch):
    if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
        print(f"{ch} is an alphabet.")
    else:
        print(f"{ch} is not an alphabet.")
ch = input("Enter a character: ")
alphabet(ch)