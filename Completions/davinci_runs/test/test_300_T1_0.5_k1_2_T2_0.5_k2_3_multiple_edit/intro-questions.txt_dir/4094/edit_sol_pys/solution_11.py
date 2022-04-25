

def main():
    n = int(input().strip())
    s = list(map(int, input().strip().split()))
    d, m = map(int, input().strip().split())
    ans = 0
    for i in range(n - m + 1):
        if sum(s[i:i + m]) == d:
            ans += 1
    print(ans)

def main2():
    k = int(sys.stdin.readline().strip())
    i = 1
    while True:
        if not (7 * (10 ** i) - 7) % k:
            print(i + 1)
            break
        i += 1

if __name__ == '__main__':
    main()
