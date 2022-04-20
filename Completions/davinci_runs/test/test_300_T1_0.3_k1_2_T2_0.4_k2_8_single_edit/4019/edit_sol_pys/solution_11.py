

def main():
    n, m, d = map(int, raw_input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    if d == 0:
        print('YES')
        for i in range(2, n+1):
            print(str(1) + " " + str(i))
    elif d == n-1:
        print('YES')
        for i in range(2, n+1):
            print(str(i-1) + " " + str(i))
    else:
        print('NO')

if __name__ == '__main__':
    main()
