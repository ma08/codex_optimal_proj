
def main():
    n, a, b = map(int, input().split())
    s = [int(input()) for i in range(n)]
    ans = 0
    i = 0
    while i < n:
        if s[i] == 1:
            if a > 0:
                a -= 1
            elif b > 0:
                b -= 1
            ans += 1
        i += 1
    print(ans)

if __name__ == "__main__":
    main()
