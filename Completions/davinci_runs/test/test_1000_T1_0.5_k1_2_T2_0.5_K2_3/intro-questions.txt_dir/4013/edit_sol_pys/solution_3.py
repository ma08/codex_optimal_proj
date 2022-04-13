import sys
input = sys.stdin.readline



def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if m == 1:
        print(a[0] + b[0])
        exit()
    ans = 0
    for i in range(n):
        c = a[i] + b[0]
        for j in range(1, m):
            d = a[i] + b[j]
            if c < d:
                c = d
        ans += c
    print(ans)


if __name__ == "__main__":
    main()
