def note(num):
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    print(f"Total notes for {num}:")
    for n in notes:
        count = num // n
        if count > 0:
            print(f"{n} : {count}")
            num = num % n
num = int(input("Enter the amount: "))
note(num)
