def is_valid(n):
    return n == 1 or n == 0 or n == 2


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

    e = int(input())
    input_validation(e)
    f = int(input())
    input_validation(f)
    g = int(input())
    input_validation(g)
    h = int(input())
    input_validation(h)

    if a == b == c == d == e == f == g == h == 0:
        print(0)
    elif a == b == c == d == e == f == g == h == 1:
        print(1)
    elif a == b and c == d and e == f and g == h:
        print(1)
    elif a == c and b == d and e == g and f == h:
        print(1)
    elif a == d and b == c and e == h and f == g:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
