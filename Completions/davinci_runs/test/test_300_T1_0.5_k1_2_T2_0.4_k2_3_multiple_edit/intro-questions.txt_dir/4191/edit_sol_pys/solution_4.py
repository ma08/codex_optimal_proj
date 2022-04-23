def is_valid(n):
    return n == 1 or n == 0


def input_validation(n):
    if not is_valid(n):
        print("Invalid input!")
        exit(1)


def main():
    a, b, c, d = [int(input()) for _ in range(4)]
    for number in [a, b, c, d]:
        input_validation(number)

    if a == b == c == d == 0:
        print(0)
    elif a == b == c == d == 1:
        print(1)
    elif a == b and c == d:
        print(1)
    elif a == c and b == d:
        print(1)
    elif a == d and b == c:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
