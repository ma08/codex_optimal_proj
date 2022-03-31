

def solve(s):
    if len(s) == 1:
        return 'YES\n0'
    n = len(s)
    s = list(s)
    ans = [0] * n
    for i in range(1, n):
        if s[i] < s[i-1]:
            ans[i] = 1
            s[i] = chr(ord(s[i]) + 2)
    for i in range(1, n):
        if s[i] < s[i-1]:
            return 'NO'
    return 'YES\n' + ''.join(map(str, ans))

n = int(input())
s = input()
print(solve(s))