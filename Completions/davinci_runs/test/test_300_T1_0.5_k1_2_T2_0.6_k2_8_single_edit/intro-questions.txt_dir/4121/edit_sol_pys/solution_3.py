
from collections import Counter

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a)
    mn = min(a)
    if mx == mn:
        print('YES')
        return
    if mx - mn > 1:
        print('NO')
        return
    c = Counter(a)
    if c[mx] > 1 and c[mn] > 1:
        print('NO')
        return
    print('YES')


if __name__ == "__main__":
    main()
