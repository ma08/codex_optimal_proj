

def main():
    n = int(input())
    a = list(map(int, input().split())) + [0]
    ans = 0

    for i in range(n):
        if a[i] < a[i + 1]:
            ans += a[i + 1] - a[i]

    print(ans)


if __name__ == "__main__":
    main()
