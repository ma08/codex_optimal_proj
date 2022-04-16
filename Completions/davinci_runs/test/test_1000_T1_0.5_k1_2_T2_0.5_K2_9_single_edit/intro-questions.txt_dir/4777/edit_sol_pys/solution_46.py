

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    k = int(input()) - 1
    a = fib(k + 1) - 1
    b = fib(k) - 1
    print(a, b)

main()
