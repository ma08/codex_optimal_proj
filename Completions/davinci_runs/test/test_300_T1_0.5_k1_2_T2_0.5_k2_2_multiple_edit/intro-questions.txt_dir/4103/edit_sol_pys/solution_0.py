

def main():
    n, b, a = map(int, input().split())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if s[i] == 1:
            if a < b and a > 0:
                a += 1
            else:
                b += 1
        if a > 0:
            a -= 1
            ans += 1
        elif b > 0:
            b -= 1
            ans += 1
        else:
            break
    print(ans)

if __name__ == "__main__":
    main()
