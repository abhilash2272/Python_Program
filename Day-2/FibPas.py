def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci series up to", n, "terms:")
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()
def pascal_triangle(n):
    print("\nPascal's Triangle up to", n, "rows:")
    for i in range(n):
        print(' ' * (n - i), end='')
        val = 1
        for j in range(i + 1):
            print(val, end=' ')
            val = val * (i - j) // (j + 1)
        print()
terms = int(input("Enter number of terms/rows: "))
fibonacci(terms)
pascal_triangle(terms)