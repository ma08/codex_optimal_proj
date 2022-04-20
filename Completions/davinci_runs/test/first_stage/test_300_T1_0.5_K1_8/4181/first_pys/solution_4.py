

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        a[i+1] -= min(a[i], b[i])
        a[i+1] = max(a[i+1], 0)
        ans += min(a[i+1], b[i])
    print(ans)

if __name__ == '__main__':
    main()