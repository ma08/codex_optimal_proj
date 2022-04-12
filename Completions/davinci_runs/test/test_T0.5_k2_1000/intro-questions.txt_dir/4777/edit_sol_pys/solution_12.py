

def fib(k):
    if k <= 1:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)

def main():
    k = int(raw_input())
    a = fib(k + 1) - 1
    b = fib(k) - 1
    print a, b

main()
