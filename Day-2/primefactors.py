def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def pf(n):
    for i in range(2, n):
        if n % i == 0 and is_prime(i):
            print(f"{i}", end=" ")

n = int(input("Enter number: "))
pf(n) 