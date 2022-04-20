import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs(x-1, y)
    if y > 0:
        dfs(x, y-1)


def dfs2(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs2(x-1, y)
    if y > 0:
        dfs2(x, y-1)


def dfs3(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs3(x-1, y)
    if y > 0:
        dfs3(x, y-1)


def dfs4(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs4(x-1, y)
    if y > 0:
        dfs4(x, y-1)


def dfs5(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs5(x-1, y)
    if y > 0:
        dfs5(x, y-1)


def dfs6(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs6(x-1, y)
    if y > 0:
        dfs6(x, y-1)


def dfs7(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs7(x-1, y)
    if y > 0:
        dfs7(x, y-1)


def dfs8(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs8(x-1, y)
    if y > 0:
        dfs8(x, y-1)


def dfs9(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs9(x-1, y)
    if y > 0:
        dfs9(x, y-1)


def dfs10(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs10(x-1, y)
    if y > 0:
        dfs10(x, y-1)


def dfs11(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs11(x-1, y)
    if y > 0:
        dfs11(x, y-1)


def dfs12(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs12(x-1, y)
    if y > 0:
        dfs12(x, y-1)


def dfs13(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs13(x-1, y)
    if y > 0:
        dfs13(x, y-1)


def dfs14(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs14(x-1, y)
    if y > 0:
        dfs14(x, y-1)


def dfs15(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs15(x-1, y)
    if y > 0:
        dfs15(x, y-1)


def dfs16(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs16(x-1, y)
    if y > 0:
        dfs16(x, y-1)


def dfs17(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs17(x-1, y)
    if y > 0:
        dfs17(x, y-1)


def dfs18(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs18(x-1, y)
    if y > 0:
        dfs18(x, y-1)


def dfs19(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs19(x-1, y)
    if y > 0:
        dfs19(x, y-1)


def dfs20(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs20(x-1, y)
    if y > 0:
        dfs20(x, y-1)


def dfs21(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs21(x-1, y)
    if y > 0:
        dfs21(x, y-1)


def dfs22(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs22(x-1, y)
    if y > 0:
        dfs22(x, y-1)


def dfs23(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs23(x-1, y)
    if y > 0:
        dfs23(x, y-1)


def dfs24(x, y):
    global ans
    if x == 0 and y == 0:
        ans += 1
        return
    if x > 0:
        dfs24(x-1, y)
    if y > 0:
        dfs24(x, y-1)


def dfs25(x, y


n = int(input())
x = list(map(int, input().split()))

x.sort()

ans = 0
for i in range(1, n):
    if x[i] - x[i-1] > 1:
        ans += x[i] - x[i-1] - 1

print(ans)
