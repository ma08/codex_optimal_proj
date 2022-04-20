

n = int(input())
arr = list(map(int, input().split()))

memo = {}

def solve(i, j, curr):
    if (i, j) in memo:
        return memo[(i, j)]

    if i == j:
        return [(i, j)]

    ans = []
    if arr[i] == curr:
        ans += solve(i+1, j, curr)
    if arr[j] == curr:
        ans += solve(i, j-1, curr)

    for k in range(i+1, j):
        if arr[k] == curr:
            left = solve(i, k-1, curr)
            right = solve(k+1, j, curr)
            ans += left + right
            break

    memo[(i, j)] = ans
    return ans


ans = solve(0, n-1, arr[0])
print(len(ans))
for a in ans:
    print(a[0]+1, a[1]+1)