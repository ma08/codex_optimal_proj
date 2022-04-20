

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    ans = 0
    for i in range(n):
        if i < k:
            if t[i] == 'r':
                ans += p
            elif t[i] == 's':
                ans += r
            else:
                ans += s
        else:
            if t[i-k] == t[i]:
                t[i] = 'x'
            else:
                if t[i] == 'r':
                    ans += p
                elif t[i] == 's':
                    ans += r
                else:
                    ans += s
    print(ans)

if __name__ == '__main__':
    main()
