import sys
sys.setrecursionlimit(10**6)

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    b.sort()
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] == b[j]:
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    if i == n:
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    main()
