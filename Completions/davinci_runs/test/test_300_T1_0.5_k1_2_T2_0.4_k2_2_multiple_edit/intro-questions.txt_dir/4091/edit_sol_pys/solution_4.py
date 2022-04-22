
def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= i+1
    a.sort()
    b = a[n//2]
    ans = 0
    for i in range(n):
        ans += abs(a[i]-b)
    print(ans)

main()
