

def solve():
    n = int(input())
    a = sorted(map(int, input().split()))
    ans = 1
    for i in range(1, n):
        if a[i] - a[i-1] <= 5:
            ans += 1
        else:
            break
    print(ans)

solve()