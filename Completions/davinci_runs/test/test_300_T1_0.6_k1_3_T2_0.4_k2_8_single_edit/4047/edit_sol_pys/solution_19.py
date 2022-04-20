

def solve(n, x):
    m = min(x)
    x = [i - m for i in x]
    x.sort()
    s = sum(x)
    if s % n:
        return -1
    s //= n
    if x[0] == x[-1]:
        return 0
    c = 0
    for i in x:
        c += abs(i - s)
    return c//2

def main():
    n = int(input())
    x = list(map(int, input().split()))
    print(solve(n, x))

if __name__ == '__main__':
    main()
