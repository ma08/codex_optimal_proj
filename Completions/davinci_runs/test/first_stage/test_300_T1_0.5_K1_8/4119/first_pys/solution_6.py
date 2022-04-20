

def main():
    n, m = list(map(int, input().split()))
    x = list(map(int, input().split()))
    x = sorted(x)
    ans = 0
    for i in range(1, m):
        ans += max(0, x[i] - x[i-1] - 1)

    print(ans)

if __name__ == '__main__':
    main()