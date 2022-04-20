
#
# Solution

def solve(n, m, a):
    a.sort(key=lambda x: x[0])
    ans = 0
    for i in range(1, n):
        ans = max(ans, a[i][0] - a[i-1][0])
    return ans

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    print(solve(n, m, a))
