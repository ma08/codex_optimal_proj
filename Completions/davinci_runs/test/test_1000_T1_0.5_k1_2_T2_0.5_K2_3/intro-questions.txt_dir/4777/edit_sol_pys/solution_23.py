

def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    k = int(input())
    a = fibonacci(k + 1)
    b = fibonacci(k)
    print(a, b)

main()
