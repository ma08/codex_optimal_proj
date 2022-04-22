from collections import defaultdict, deque



def solve(n, k, a):
    d = defaultdict(int)
    for i in range(n):
        if d[a[i]] == 0:
            d[a[i]] = 1
        else:
            d[a[i]] += 1

    print(d)
    return 0


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(n, k, a))
