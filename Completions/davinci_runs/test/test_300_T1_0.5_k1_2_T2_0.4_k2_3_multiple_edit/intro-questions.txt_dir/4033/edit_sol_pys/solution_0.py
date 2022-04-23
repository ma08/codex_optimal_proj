

def main():
    a, b = map(int, input().split())

    if a == b:
        print(a*4)
        return

    if a < b:
        a, b = b, a

    # a > b
    if (a+b) % 3 == 0:
        print((a+b)*2//3*2)
    else:
        print((a+b)*2//3*2+2)


if __name__ == "__main__":
    main()
