
def is_valid(n):
    return n == 1 or n == 0 or n == -1


def input_validation(n):
    if not is_valid(n):
        print("Invalid input!")
        exit(1)


def main():
    a = int(input())
    input_validation(a)
    b = int(input())
    input_validation(b)
    c = int(input())
    input_validation(c)
    d = int(input())
    input_validation(d)

    input_validation(d)

    if a == b and c == d:
        print(a + c)
    elif a == c and b == d:
        print(a + b)
    elif a == d and b == c:
        print(a + b)
    else:
        print(a + b + c + d)


if __name__ == '__main__':
    main()
