

def main():
    a, b = map(int, input().split())

    if a == b:
        print(4*a)
        return

    if a < b:
        a, b = b, a

    # a > b
    if (a+b) % 3 == 0:
        print(2*(a+b)//3)
    else:
        print((a+2*b)//3)


if __name__ == "__main__":
    main()
