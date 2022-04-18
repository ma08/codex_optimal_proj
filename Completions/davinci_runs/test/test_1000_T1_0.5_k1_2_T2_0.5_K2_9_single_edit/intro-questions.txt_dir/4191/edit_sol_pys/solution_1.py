
def is_valid(n):
    return n == 1 or n == 0



def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    if not is_valid(a):
        print("Invalid input!")
        exit(1)
    if not is_valid(b):
        print("Invalid input!")
        exit(1)
    if not is_valid(c):
        print("Invalid input!")
        exit(1)
    if not is_valid(d):
        print("Invalid input!")
        exit(1)

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
