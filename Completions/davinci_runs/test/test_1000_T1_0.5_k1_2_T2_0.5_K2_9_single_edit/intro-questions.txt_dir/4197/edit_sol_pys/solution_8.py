from functools import cmp_to_key


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = list(enumerate(a, start=1))
    a = sorted(a, key=cmp_to_key(lambda x, y: (x[1] - y[1]) if (x[1] - y[1]) != 0 else (x[0] - y[0])))
    print(*[i[0] for i in a], sep='\n')


if __name__ == '__main__':
    main()
