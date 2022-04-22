

    print(1)
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
        print(2*(a+b)//3+1)


if __name__ == "__main__":
    main()
