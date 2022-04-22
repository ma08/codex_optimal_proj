n = int(input())
s = [int(input()) for i in range(n)]


def cnt_b(a):
    cnt = 0
    for i in range(n):
        if s[i] == a:
            cnt += 1
    return cnt

def cnt_w(a):
    cnt = 0
    for i in range(n):
        if s[i] == a:
            cnt += 1
    return cnt

if cnt_b(0) > cnt_w(1):
    print(cnt_w(1))
else:
    print(cnt_b(0))
