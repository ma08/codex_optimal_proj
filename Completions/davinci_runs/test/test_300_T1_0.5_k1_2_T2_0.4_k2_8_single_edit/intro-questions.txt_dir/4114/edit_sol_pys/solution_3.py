import sys



def main():
    n = int(input())
    for i in range(1, n + 1):
        print("Case #{}: ".format(i), end="")
        solve()


def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = sorted(a)
    b = sorted(b)
    if a[-1] + b[-1] < k:
        print("IMPOSSIBLE")
        return
    print("POSSIBLE")
    for i in range(n):
        print("".join(["1" if a[i] + b[j] >= k else "0" for j in range(n)]))


if __name__ == "__main__":
    main()
