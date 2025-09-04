def palin(n):
    for num in range(1, n + 1):
        if str(num) == str(num)[::-1]:
            print(num, end=' ')

n = int(input("Enter n: "))
palin(n)