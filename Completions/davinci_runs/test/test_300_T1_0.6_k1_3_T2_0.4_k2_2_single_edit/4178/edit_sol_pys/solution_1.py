

import sys

sys.setrecursionlimit(10 ** 8)


def read_ints():
    return list(map(int, sys.stdin.readline().split()))


def read_a_int():
    return int(sys.stdin.readline())


def read_tuple(H):
    '''
    H is number of rows
    '''
    ret = []
    for _ in range(H):
        ret.append(tuple(map(int, sys.stdin.readline().split())))
    return ret


def read_col(H):
    '''
    H is number of rows
    A列、B列が与えられるようなとき
    ex1)A,B=read_col(H)    ex2) A,=read_col(H) #一列の場合
    '''
    ret = []
    for _ in range(H):
        ret.append(list(map(int, sys.stdin.readline().split())))
    return tuple(map(list, zip(*ret)))


def read_matrix(H):
    '''
    H is number of rows
    '''
    ret = []
    for _ in range(H):
        ret.append(list(map(int, sys.stdin.readline().split())))
    return ret


def read_map(H):
    '''
    H is number of rows
    文字列で与えられた盤面を読み取る用
    '''
    return [sys.stdin.readline().strip() for _ in range(H)]


def read_map_as_int(H):
    '''
    #→1,.→0として読み込む
    '''
    ret = []
    for _ in range(H):
        ret.append([1 if s == '#' else 0 for s in sys.stdin.readline().strip()])
    return ret


def read_map_as_char(H):
    '''
    文字で与えられた盤面を読み取る用
    '''
    ret = []
    for _ in range(H):
        ret.append([c for c in sys.stdin.readline().strip()])
    return ret


def read_matrix(H):
    '''
    H is number of rows
    '''
    ret = []
    for _ in range(H):
        ret.append(list(map(int, sys.stdin.readline().split())))
    return ret


def read_tuple(H):
    '''
    H is number of rows
    '''
    ret = []
    for _ in range(H):
        ret.append(tuple(map(int, sys.stdin.readline().split())))
    return ret


def read_col(H):
    '''
    H is number of rows
    A列、B列が与えられるようなとき
    ex1)A,B=read_col(H)    ex2) A,=read_col(H) #一列の場合
    '''
    ret = []
    for _ in range(H):
        ret.append(list(map(int, sys.stdin.readline().split())))
    return tuple(map(list, zip(*ret)))


def read_col_tuple(H):
    '''
    H is number of rows
    '''
    ret = []
    for _ in range(H):
        ret.append(tuple(map(int, sys.stdin.readline().split())))
    return tuple(map(list, zip(*ret)))


def read_col_tuple_as_int(H):
    '''
    H is number of rows
    '''
    ret = []
    for _ in range(H):
        ret.append([1 if s == '#' else 0 for s in sys.stdin.readline().split()])
    return tuple(map(list, zip(*ret)))


def read_matrix(H):
    '''
    H is number of rows
    '''
    ret = []
    for _ in range(H):
        ret.append(list(map(int, sys.stdin.readline().split())))
    return ret


MOD = 10**9 + 7
INF = 2**31  # 2147483648 > 10**9
# default import
from collections import defaultdict, Counter, deque
from operator import itemgetter
from itertools import product, permutations, combinations
from bisect import bisect_left, bisect_right  # , insort_left, insort_right

# https://atcoder.jp/contests/abc141/tasks/abc141_e
# 右に伸ばしていって、そのときに何個かぶっているかを求める
# 同じ文字がいくつかぶっているときは、それらの中で最も左にあるものを採用する
# その最も左にあるものを採用するとき、その文字列の長さが最大になる

N = read_a_int()
S = read_map_as_char(N)

# dp[i][j] := S[i]とS[j]が一致しているか
dp = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if S[i][j] == S[i][j]:
            dp[i][j] = 1

# print(dp)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if dp[i][j] and dp[j][k]:
                ans = max(ans, k - i)
print(ans)

ans = True
