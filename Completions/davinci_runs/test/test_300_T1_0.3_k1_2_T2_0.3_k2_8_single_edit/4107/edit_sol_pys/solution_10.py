
def main():
    n, k = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n):
        if s[i] == '1':
            ans += i + 1
        else:
            ans += min(i + 1, n - i)
    print(ans)

if __name__ == "__main__":
    main()
