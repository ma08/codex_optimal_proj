
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        ans = 0
        for i in range(1, n):
            if a[i] - a[i-1] > 1:
                ans = a[i-1] + 1
                break
        if ans == 0:
            ans = a[-1] + 1
        print(ans)
if __name__ == '__main__':
    main()
