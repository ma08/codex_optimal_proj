

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def last_digit(n):

    return factorial(n) % 10

def main():
    num_case = int(input().strip())
    for i in range(num_case):
        n = int(input().strip())
        print(last_digit(n))


if __name__ == '__main__':
    main()
