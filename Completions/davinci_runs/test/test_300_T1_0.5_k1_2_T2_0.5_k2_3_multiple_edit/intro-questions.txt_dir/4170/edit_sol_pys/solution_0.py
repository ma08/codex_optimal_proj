
def main():
    n = int(input())
    hs = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if hs[i] >= hs[i+1]:
            ans += hs[i] - hs[i+1] + 1
            hs[i+1] = hs[i] + 1
    ans += hs[-1]
    print(ans)

if __name__ == '__main__':
    main()
