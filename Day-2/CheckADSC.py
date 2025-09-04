def check(ch):
    if ch.isdigit():
        print(f"{ch} is a digit")
    elif ch.isalpha():
        print(f"{ch} is a character")
    else:
        print(f"{ch} is a special character")
ch=input("Enter a character ")
check(ch)
