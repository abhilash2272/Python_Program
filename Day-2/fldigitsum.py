def digit(n):
    last = n % 10
    print(f"{last} is the last digit")
    first = n
    while first >= 10:
        first = first // 10
    print(f"{first} is the first digit")
    print(f"sum is{first+last}")
n = int(input("Enter number: "))
digit(n)