
def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0 or h[i-1] <= h[i]:
            ans = max(ans, h[i])
        else: ans = max(ans, h[i-1]-1)
    print(ans)

if __name__ == '__main__':
    main()
