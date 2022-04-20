

def main():
    n, m, d = map(int, input().split())  # n: number of vertices, m: number of edges, d: diameter
    edges = [tuple(map(int, input().split())) for _ in range(m)]  # edges

    if d == 0:  # diameter is 0
        print('YES')
        for i in range(2, n+1):
            print(1, i)
    elif d == n-1:  # diameter is n-1
        print('YES')
        for i in range(2, n+1):
            print(i-1, i)
    else:  # diameter is not 0 or n-1
        print('NO')

if __name__ == '__main__':
    main()
