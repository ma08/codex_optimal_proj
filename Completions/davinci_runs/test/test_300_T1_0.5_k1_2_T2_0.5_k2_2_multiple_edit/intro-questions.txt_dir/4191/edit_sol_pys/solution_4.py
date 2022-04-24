def is_valid(n):
    return n == 1 or n == 0 or n == 2


def input_validation(n):
    if not is_valid(n):
        print("Invalid input!")
        exit(1)


def main():
    a = input_validation(int(input()))
    b = input_validation(int(input()))
    c = input_validation(int(input()))
    d = input_validation(int(input()))

    if a == 0 and b == 0 and c == 0 and d == 0:
        print(0)
    elif a == 1 and b == 1 and c == 1 and d == 1:
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
