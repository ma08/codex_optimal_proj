

def main():
    n, a, b = map(int, input().split())
    s = list(map(int, input().split())).reverse()
    ans = 0
    while len(s) > 0:
        if s[-1] == 0:
            if a > 0:
                a -= 1
                ans += 1
            elif b > 0:
                b -= 1
                ans += 1
            else:
                break
        else:
            if b > 0:
                b -= 1
                ans += 1
            else:
                break
        s.pop()
    print(ans)

if __name__ == "__main__":
    main()
