

def solve(n, a, m):
    count = 0
    s = 0
    h = {}
    h[0] = -1
    for i in range(n):
        s += a[i]
        if s == m:
            count += 1
            s = 0
        if s in h and h[s] < i and s != 0:
            count += 1
            s = 0
        h[s] = i
    return count

def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    print(solve(n, a, m))

if __name__ == '__main__':
    main()
