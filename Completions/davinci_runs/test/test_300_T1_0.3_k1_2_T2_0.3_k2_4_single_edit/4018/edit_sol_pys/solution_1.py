

def main():
    n, k = map(int, input().split())
    s = input()
    if k > 2 ** n:
        print(-1)
        return
    ans = 0
    for i in range(n):
        if k % 2 == 1:
            ans += n - i
            k -= 1
        k //= 2
    print(ans)


if __name__ == '__main__':
    main()
