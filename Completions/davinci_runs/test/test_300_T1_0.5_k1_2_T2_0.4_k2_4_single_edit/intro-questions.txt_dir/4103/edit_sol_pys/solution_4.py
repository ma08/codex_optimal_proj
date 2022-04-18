

def main():
    n, b, a = map(int, input().split())
    s.reverse()
    s = list(map(int, input().split()))
    ans = 0
    # print(s)
    i = 0
    while i < n:
        if s[i] == 1:
            if a == 0:
                b += 1
            elif b == 0:
            elif a < b:
                b += 1
                a += 1
            else:
                a += 1
        # print(a, b)
        if a > 0:
            a -= 1
        elif b > 0:
            b -= 1
        else:
            break
        ans += 1
        i += 1
    print(ans)

if __name__ == "__main__":
    main()
