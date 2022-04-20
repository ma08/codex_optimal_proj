

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
            for j in range(max(0, i-k), min(n, i+k+1)):
                    s[j] = 0
    print(ans)

if __name__ == '__main__':
    main()
