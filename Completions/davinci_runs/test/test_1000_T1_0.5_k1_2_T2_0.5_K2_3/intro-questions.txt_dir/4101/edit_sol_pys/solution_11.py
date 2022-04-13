

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)] # list comprehension
    r, c = [], []
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                r.append(i)
                c.append(j)
                break
    if len(r) == n:
        print('YES')
        print('0 '*n) # print 0 n times
        print('0 '*m) # print 0 m times
    elif len(c) == m:
        print('YES')
        print('1 '*n) # print 1 n times
        print('0 '*m) # print 0 m times
    else:
        print('NO')

if __name__ == '__main__':
    main()
