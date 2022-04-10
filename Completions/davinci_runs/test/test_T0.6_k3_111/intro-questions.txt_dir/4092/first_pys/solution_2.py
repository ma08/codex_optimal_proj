

def solve(n, a):
    count = 0
    s = 0
    h = {}
    # h[0] = -1
    for i in range(n):
        s += a[i]
        if s == 0:
            count += 1
            s = 1
        if s in h:
            count += 1
            s = 1
        h[s] = i
    return count

def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    print(solve(n, a))

if __name__ == '__main__':
    main()