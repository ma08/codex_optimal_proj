

def main():
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    a = [a[i] + i for i in range(n)]
    if a[-1] < m:
        print(-1)
    else:
        print(min(a.index(m) + 1, n))

if __name__ == '__main__':
    main()