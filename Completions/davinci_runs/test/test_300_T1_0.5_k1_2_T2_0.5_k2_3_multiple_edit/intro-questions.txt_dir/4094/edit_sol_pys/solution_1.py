

def main():
    k = int(input().strip())
    i = 1
    while True:
        if not (7 * (10 ** i) - 7) % k:
            print(i + 1)
            break
        i += 1

def main2():
    n = int(input().strip())
    s = list(map(int, input().strip().split()))
    d, m = map(int, input().strip().split())
    ans = 0
    for i in range(n - m + 1):
        if sum(s[i:i + m]) == d:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
