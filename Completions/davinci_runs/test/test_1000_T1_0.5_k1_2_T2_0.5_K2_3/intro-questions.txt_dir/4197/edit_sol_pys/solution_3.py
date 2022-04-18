# testing


def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = list(enumerate(a, 1))
    x = sorted(x, key=lambda x: x[1])
    x = [i[0] for i in x]
    print(*x, sep='\n')


if __name__ == '__main__':
    main()
