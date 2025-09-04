def strong(num):
    temp = num
    sum = 0
    while temp > 0:
        r = temp % 10
        fact = 1
        for i in range(1, r + 1):
            fact *= i
        sum += fact
        temp //= 10
    return sum == num
n = int(input("Enter a number: "))
if strong(n):
    print(f"{n} is a strong number")
else:
    print(f"{n} is not a strong number")
