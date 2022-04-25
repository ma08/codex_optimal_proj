


def main():
    A, B, T = map(int, input().split())
    print(B * ((T + A - 1) // A))


if __name__ == '__main__':
    main()
