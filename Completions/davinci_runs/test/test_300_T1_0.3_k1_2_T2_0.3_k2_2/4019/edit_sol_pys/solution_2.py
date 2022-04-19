

def main():
    n, m, d = map(int, input().split())  # read input
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    if d == 0:  # if d is 0
        print('YES')
        for i in range(2, n+1):
            print(1, i)
    elif d == n-1:  # if d is n-1
        print('YES')
        for i in range(2, n+1):
            print(i-1, i)
    else:  # if d is not 0 and n-1
        print('NO')

if __name__ == '__main__':
    main()
