def prime(num):
    if num < 2:
        print(f"{num} is not a prime number.")
        return
    i = 2
    while i <= num // 2:
        if num % i == 0:
            print(f"{num} is not a prime number.")
            return
        i += 1
    print(f"{num} is a prime number.")
num = int(input("Enter a number: "))
prime(num)