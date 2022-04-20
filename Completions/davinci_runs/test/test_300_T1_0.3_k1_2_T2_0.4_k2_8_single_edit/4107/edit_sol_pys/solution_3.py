

def main():
    n, k = map(int, input().split())
    s = input()
    s = [int(i) for i in s]
    ans = 0
    for i in range(n):
        if s[i] == 0:
            ans += i + 1
    for i in range(n-k):
        if s[i] == 1 and s[i+k] == 0:
            ans += i + 1
            s[i+k] = 1
    print(ans)

if __name__ == '__main__':
    main()
