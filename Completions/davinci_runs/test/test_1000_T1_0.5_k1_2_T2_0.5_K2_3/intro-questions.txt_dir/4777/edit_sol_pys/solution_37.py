
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    n = int(input())
    a = fib(n + 1) - 1
    b = fib(n) - 1
    print(a, b)

main()
