

def fib(n):
    if n == 1:
    elif n == 2:
        return 2
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    k = int(input())
    a = fib(k + 1)
    b = fib(k)
    print(a, b)

main()
