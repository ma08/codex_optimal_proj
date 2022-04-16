

def is_square(x):
    return int(x ** 0.5) ** 2 == x


def main():
    a, b = map(int, input().split())

    if is_square(int(str(a) + str(b))):  # int(str(a) + str(b)) = a*10^len(str(b)) + b
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
