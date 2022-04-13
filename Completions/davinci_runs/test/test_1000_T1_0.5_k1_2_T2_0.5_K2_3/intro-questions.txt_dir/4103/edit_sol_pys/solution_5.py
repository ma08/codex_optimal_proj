

def main():
    n, a, b = map(int, input().split())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if s[i] == 0:
            if a == 0:
                if b == 0:
                    ans += 1
                else:
                    b -= 1
            else:
                a -= 1
        else:
            if b == 0:
                ans += 1
            else:
                b -= 1
    print(ans)

if __name__ == "__main__":
    main()
