
def main():
    n = int(input())
    hs = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if n == 0:
            ans += 1
            break
        if hs[i] >= hs[i+1]:
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
