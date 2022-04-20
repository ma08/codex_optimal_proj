
def main():
    n, m = map(int, input().split())
    ans = 0
    while n <= m:
        n *= 2
        ans += 1
    print(ans - 1)

if __name__ == '__main__':
    main()
