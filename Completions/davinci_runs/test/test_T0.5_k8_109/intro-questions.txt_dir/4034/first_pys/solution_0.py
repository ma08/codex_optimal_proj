

def color_string(s):
    n = len(s)
    if n == 1:
        return True, '0' * n
    if n == 2:
        return s[0] <= s[1], '0' + '1'
    if n == 3:
        return s[0] <= s[1] and s[1] <= s[2], '0' + '1' * (n - 2)
    if s[0] > s[1]: return False, ''
    if s[-2] > s[-1]: return False, ''
    for i in range(1, n - 1):
        if s[i - 1] > s[i] and s[i] > s[i + 1]: return False, ''
    ans = ''
    for i in range(n):
        if s[i - 1] > s[i] and s[i] > s[i + 1]:
            ans += '1'
        else:
            ans += '0'
    return True, ans

n = int(input())
s = input()

ans = color_string(s)
print(ans[0])
if ans[0]:
    print(ans[1])