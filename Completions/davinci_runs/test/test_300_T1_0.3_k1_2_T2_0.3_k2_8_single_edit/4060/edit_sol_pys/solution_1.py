
n = int(input())
s = input()

def is_regular(s1):
    cnt = 0
    for i in s1:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0

    if is_regular(s1):
        return 0
    cnt = 0
    for i in s1:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == -1:
            return 1
    return 1

print(solve(s))
