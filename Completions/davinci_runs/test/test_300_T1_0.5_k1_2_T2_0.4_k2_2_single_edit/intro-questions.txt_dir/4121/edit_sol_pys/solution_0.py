from collections import Counter



def main():
    n, m = map(int, input().split())
    a = Counter(map(int, input().split()))
    b = Counter(map(int, input().split()))
    c = Counter(a.keys() & b.keys())
    ans = 0
    for k, v in c.items():
        ans += min(a[k], b[k])
    print(ans)


if __name__ == "__main__":
    main()
