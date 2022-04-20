
n = int(input())
s = input()


def is_regular(string):
    cnt = 0
    for i in string:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0


def solve(string):
    if is_regular(string):
        return 0
    cnt = 0
    for i in string:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == -1:
            return 1
    return 1


print(solve(s))
