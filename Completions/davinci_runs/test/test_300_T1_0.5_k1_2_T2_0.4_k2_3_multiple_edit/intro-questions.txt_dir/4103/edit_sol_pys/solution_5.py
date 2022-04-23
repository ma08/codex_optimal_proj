

def main():
    n, a, b = map(int, input().split())
    s = list(map(int, input().split()))[::-1]
    ans = 0
    for i in range(n):
        if s[i] == 1:
            if a > 0:
                a -= 1
                ans += 1
            elif b > 0:
                b -= 1
                ans += 1
            elif a == 0 and b == 0:
                break
            else:
                continue
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
        i += 1
    print(ans)

if __name__ == "__main__":
    main()
