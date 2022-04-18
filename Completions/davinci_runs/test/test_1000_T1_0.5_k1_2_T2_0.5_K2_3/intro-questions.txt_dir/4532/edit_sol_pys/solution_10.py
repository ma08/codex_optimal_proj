
def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        ans = 0
        for j in range(n):
            if a[j] % k != 0:
                if a[j] % k > k // 2:
                    ans += k - a[j] % k
                    a[j] += ans
                else:
                    ans += a[j] % k
                    a[j] += ans
        print(ans)

if __name__ == "__main__":
    main()
