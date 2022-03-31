
def solve(s):
    n = len(s)
    s = list(s)
    ans = [0] * (n-1)
    for i in range(1, n):
        if s[i] < s[i-1]:
            ans[i] = 1
            s[i] = chr(ord(s[i]) + 1)
    for i in range(1, n):
        if s[i] < s[i-1]:
            return 'NO'
    return 'YES\n' + ' '.join(map(str, ans))

n = int(input())
s = input()
print(solve(s))
