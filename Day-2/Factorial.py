def fact(n):
    result = 1
    print(f"{n} =", end=' ')
    i = n
    while i > 0:
        print(i, end='*' if i > 1 else '')
        result *= i
        i -= 1
    print(f"\nFactorial of {n} is {result}")
num = int(input("Enter the number: "))
fact(num)