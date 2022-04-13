

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        ans += max(0, 80 - a[i])

    print(ans)

if __name__ == "__main__":
    main()
