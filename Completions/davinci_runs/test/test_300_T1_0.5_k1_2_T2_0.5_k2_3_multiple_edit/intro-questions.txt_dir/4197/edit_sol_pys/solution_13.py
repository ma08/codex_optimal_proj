


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(enumerate(a, 1), key=lambda x: x[1])
    print(*[i[0] for i in a], sep='\n')


if __name__ == '__main__':
    main()
