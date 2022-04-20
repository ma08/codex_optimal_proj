
def is_regular(s):
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0

def solve(s):
    if is_regular(s):
        return 0
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == -1:
            return 1
    return 1


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(solve(s))
