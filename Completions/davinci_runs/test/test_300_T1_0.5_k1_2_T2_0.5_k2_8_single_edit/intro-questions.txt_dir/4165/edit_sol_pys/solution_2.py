import sys
sys.setrecursionlimit(10 ** 7)


read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 20min
# 右に移動していく -> 左に移動していく

N, K = map(int, input().split())
A = list(map(int, input().split()))


def is_ok(A, k):
    for i in range(N - k):
        if A[i] > A[i + k]:
            return False
    return True


def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(A, mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(0, N))
