def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0 or a[i] % 3 == 2:
            a[i] -= 1
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
