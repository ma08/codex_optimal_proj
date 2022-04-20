

def main():
    n, b, a = map(int, input().split())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if s[i] == 1:
            if a < 1:
                if b < 1:
                    break
                b -= 1
            else:
                a -= 1
                b += 1
        else:
            if a < 1:
                if b < 1:
                    break
                b -= 1
            else:
                a -= 1
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()