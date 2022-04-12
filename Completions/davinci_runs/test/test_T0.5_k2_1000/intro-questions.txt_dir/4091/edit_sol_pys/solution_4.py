

def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i]*(n-i)
    print(ans)

main()
