


def main():
    n = int(input())
    b = list(map(int, input().split()))
    b = sorted(enumerate(b, 1), key=lambda x: x[1])
    b = [i[0] for i in enumerate(b, 1)]
    print(*b, sep='\n')


if __name__ == '__main__':
    main()
