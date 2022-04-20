

def main():
    n, k = map(int, input().split())
    s = input()
    s = [int(i) for i in s]
    ans = 0
    for i in range(n-k+1):
        if s[i] == 1 and s[i+k-1] == 1:
            ans += 1
            for j in range(i, i+k):
                s[j] = 0
    print(ans)

if __name__ == '__main__':
    main()
