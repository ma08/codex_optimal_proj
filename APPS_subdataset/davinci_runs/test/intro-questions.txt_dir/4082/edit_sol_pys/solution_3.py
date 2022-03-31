
n = int(input())
a = list(map(int, input().split()))

def solve(n, a):
    left = 0
    right = 0
    max_len = 0
    while right < n-1:
        if a[right+1] > a[right]:
            right += 1
        else:
            max_len = max(max_len, right-left+1)
            left = right
            right += 1
    max_len = max(max_len, right-left+1)
    return max_len

print(solve(n, a))
