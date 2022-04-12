

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

def last_digit_recursive(n):
    return factorial_recursive(n) % 10


def last_digit_iterative(n):
    return factorial_iterative(n) % 10


def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        n = int(input().strip())
        print(last_digit_recursive(n))


if __name__ == '__main__':
    main()
