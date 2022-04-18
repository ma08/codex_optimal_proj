
n = int(input())
s = input()

def solve(n, s):
    if n == 1:
        return 1

    ans = 0
    for i in range(n - 1):
        if s[i] > s[i + 1]:
            ans += 1
    return ans

print(solve(n, s))
