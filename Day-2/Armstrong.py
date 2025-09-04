def armstrong(n):
    for num in range(1, n + 1):
        temp = num
        sum = 0
        while temp > 0:
            r = temp % 10
            sum += r ** 3
            temp //= 10
        if sum == num:
            print(num, end=' ')
n = int(input("Enter n: "))
armstrong(n)