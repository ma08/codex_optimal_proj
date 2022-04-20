

def main():
    n, m, d = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    if d == 0:
        print('YES')
        for i in range(2, n+1):
            print(1, i)
    elif d == n-1:
        print('YES')
        for i in range(2, n+1):
            print(i-1, i)
    else:
        print('NO')

if __name__ == '__main__':
    main()