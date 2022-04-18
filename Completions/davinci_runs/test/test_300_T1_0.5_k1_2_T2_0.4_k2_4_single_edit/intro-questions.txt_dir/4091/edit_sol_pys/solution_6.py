

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0]*(n+1)
    for i in range(1, n+1):
        ans[i] = max(ans[i-1], a[i-1])
    for i in range(1, n+1):
        print(ans[i], end=" ")

main()
