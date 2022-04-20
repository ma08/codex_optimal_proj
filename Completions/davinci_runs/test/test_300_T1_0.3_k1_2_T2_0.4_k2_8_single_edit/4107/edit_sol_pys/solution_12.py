

def main():
    n, k = map(int, input().split())
    s = input()
    s = [int(i) for i in s]  # list(map(int, s))
    ans = 0
    for i in range(n):
        if s[i] == 0:
            ans += i + 1
    for i in range(n):
        if s[i] == 1:
            ans += i + 1
            for j in range(i-k, i+k+1):  # range(max(i-k, 0), min(i+k+1, n))
                if j >= 0 and j < n:
                    s[j] = 0
    print(ans)

if __name__ == '__main__':
    main()
