
n = int(input())
s = input()

def solve(s):
    if is_regular(s):
        return 0
    if s[0] == ')':
        return 1
    return 1

print(solve(s))
