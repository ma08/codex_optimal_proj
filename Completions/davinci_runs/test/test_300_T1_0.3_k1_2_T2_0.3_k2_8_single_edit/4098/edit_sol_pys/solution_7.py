

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    ans = 0
    for i in range(n - 1):
        if a[i + 1] - a[i] <= 5:
            ans += 1
        else:
            ans = 0

    print(ans)

if __name__ == '__main__':
    main()
