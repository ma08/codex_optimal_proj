

def main():
    n, k = map(int, input().split())
    s = input()
    s = [0] + [int(i) for i in s]
    for i in range(1, n + 1):
        s[i] += s[i - 1]
    ans = 10**20
    for i in range(1, n + 1):
        if s[i] > k:
            ans = min(ans, (s[i] - 1) * i - (s[i] - 1 - k) * (s[i] - 1 - k + 1) // 2)
    print(ans)

if __name__ == '__main__':
    main()