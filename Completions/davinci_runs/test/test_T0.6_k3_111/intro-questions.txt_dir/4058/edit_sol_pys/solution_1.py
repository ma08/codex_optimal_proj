from collections import defaultdict

def calc(n, r, a):
    x = defaultdict(int)
    cnt = 0
    for i in range(n):
        if a[i] == 1:
            x[i] = 1
            cnt += 1
    for i in range(n - 1, -1, -1):
        for j in range(i - r + 1, i + r):
            if j in x and x[j] == 1:
                x[i] = 1
                break
    if len(x) == n:
        return cnt
    else:
        return -1

def main():
    n, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(calc(n, r, a))

if __name__ == "__main__":
    main()
