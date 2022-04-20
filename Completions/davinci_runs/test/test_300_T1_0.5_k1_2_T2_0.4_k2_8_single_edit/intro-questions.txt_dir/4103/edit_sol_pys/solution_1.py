

def main():
    n, a, b = map(int, input().split())
    cnt = 0
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if s[i] == 1: a -= 1
        else: b -= 1
        if a < 0 and b < 0:
            if s[cnt] == 1: a += 1
            else: b += 1
            cnt += 1
        ans += 1
    print(ans)

if __name__ == "__main__":
    main()
