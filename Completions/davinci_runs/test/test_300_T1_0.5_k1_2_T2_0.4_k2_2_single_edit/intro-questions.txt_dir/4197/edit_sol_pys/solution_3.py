
from collections import Counter

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:m]
    c = Counter(a)
    for i in b:
        if c[i] > 0:
            print('YES')
            print(1, i)
            break
    else:
        print('NO')


if __name__ == '__main__':
    main()
