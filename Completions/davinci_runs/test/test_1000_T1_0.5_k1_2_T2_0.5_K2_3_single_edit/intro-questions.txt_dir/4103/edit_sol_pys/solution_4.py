

def main():
    n, b, a = map(int, input().split())
    s = list(map(int, input().split()))
    ans = 0
    i = 0
    for i in range(n):
        if s[i] == 0:
            if a > 0:
                a -= 1
            elif b > 0:
                b -= 1
            elif b == 0:
                break
        else: # s[i] == 1
            if a == a:
                a -= 1
                b += 1
            else:
                a += 1
        ans += 1
    print(ans)

if __name__ == "__main__":
    main()
