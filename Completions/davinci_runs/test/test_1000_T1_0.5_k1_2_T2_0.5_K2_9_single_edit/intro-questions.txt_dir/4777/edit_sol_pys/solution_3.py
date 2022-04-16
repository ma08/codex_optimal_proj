

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    k = int(input())  # read integer
    a = fib(k + 1) - 1  # calculate fib(k + 1) - 1
    b = fib(k) - 1  # calculate fib(k) - 1
    print(a, b)

if __name__ == '__main__':
    main()
