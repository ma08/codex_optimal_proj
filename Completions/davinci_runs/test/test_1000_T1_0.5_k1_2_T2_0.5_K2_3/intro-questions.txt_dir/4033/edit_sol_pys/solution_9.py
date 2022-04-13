

def main():
    a, b, c = map(int, input().split())

    if a == b == c:
        print(3 * a)
    else:
        if a == b:
            print(2 * a + c)
        elif a == c:
            print(2 * a + b)
        elif b == c:
            print(2 * b + a)
        else:
            print(a + b + c)



if __name__ == "__main__":
    main()
