
def solve(n, k, a):
    ans = 0 
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % k == 0:
                ans += 1
    return ans
