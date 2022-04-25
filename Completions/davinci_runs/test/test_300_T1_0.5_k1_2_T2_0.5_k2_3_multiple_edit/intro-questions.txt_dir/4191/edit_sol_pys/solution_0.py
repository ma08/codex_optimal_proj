
def is_valid(n):
    return n == 1 or n == 0


def input_validate(n):
    if not is_valid(n):
        print("Invalid input!")
        exit(1)


def main():
    a = int(input())
    input_validate(a)
    b = int(input())
    input_validate(b)
    c = int(input())
    input_validate(c)
    d = int(input())
    input_validate(d)

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
