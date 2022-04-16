

def main():
    a = int(input())
    b = int(input())

    c = int(input())

    if a == b == c:
        print(a)
    elif a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    elif a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)

if __name__ == "__main__":
    main()
