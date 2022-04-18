def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(0, N, 2):
        ans += a[i + 1] - a[i]
    print(ans)



if __name__ == '__main__':
    main()
