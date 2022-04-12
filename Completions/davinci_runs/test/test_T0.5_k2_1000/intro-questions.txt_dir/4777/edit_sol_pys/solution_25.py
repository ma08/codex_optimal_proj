
def fib(n):
    a = 1
    b = 1
    for i in range(n - 1):
        a, b = b, a + b
    return a, b, a + b


def main():
    k = int(input())
    a, b, c = fib(k)
    print(a, b, c)


if __name__ == '__main__':
    main()
