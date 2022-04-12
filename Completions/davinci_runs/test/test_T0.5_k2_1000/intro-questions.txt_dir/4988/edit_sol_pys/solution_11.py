

def factorial(n):  # function for factorial
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def last_digit(n):  # function for last digit

    return factorial(n) % 10

def main():
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        print(last_digit(n))


if __name__ == "__main__":
    main()
