import sys

n, k = map(int, input().split())
a = list(map(int, input().split()))
if n == 1:
    print("YES")
    print(1)
else:
    b = [0]*n
    for i in range(n):
        if a[i] == a[0]:
            b[i] = 1
        else:
            b[i] = 2
    if a[0] in a[1:]:
        print("NO")
    else:
        print("YES")


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = sys.maxsize
    for i in range(n-1):
        ans = min(ans, abs(a[i]-a[i+1]))
    print(ans)


if __name__ == "__main__":
    main()
        print(*b)
