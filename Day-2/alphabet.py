def alphabet(ch):
    current = 'a'
    while current <= ch:
        print(current, end=' ')
        current = chr(ord(current) + 1)
    print()
ch = input("Enter an alphabet (a-z):")
alphabet(ch)
