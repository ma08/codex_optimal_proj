


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = list(enumerate(a, 1))
    a = sorted(a, key=lambda x: x[1])
    a = [str(i[0]) for i in a]
    print('\n'.join(a))


if __name__ == '__main__':
    main()
