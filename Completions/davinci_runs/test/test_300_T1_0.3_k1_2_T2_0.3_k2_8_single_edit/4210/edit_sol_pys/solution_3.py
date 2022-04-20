
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))  # list
    ans = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                if (a[i] * (10 ** len(str(a[j]))) + a[j]) % k == 0:
                    ans += 1
    print(ans)


if __name__ == "__main__":
    main()
