

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] % k == 0:
            ans += 1
        for j in range(i + 1, n):
            if (a[i] * (10 ** len(str(a[j]))) + a[j]) % k == 0:
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()
