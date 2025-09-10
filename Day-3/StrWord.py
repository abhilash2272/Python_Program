def wor():
    s = input("Enter a string: ")
    count = 1 
    s.strip() 
    for i in s:
        if i == ' ':
            count += 1
    print("Total number of words:", count)
wor()