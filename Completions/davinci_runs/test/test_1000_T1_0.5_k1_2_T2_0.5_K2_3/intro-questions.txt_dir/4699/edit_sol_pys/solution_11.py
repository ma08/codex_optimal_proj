
# N, K = map(int, input().split())
# D = set(map(int, input().split()))

# # print(N, K, D)

# for i in range(N, 10000):
#     if all(d not in str(i) for d in D):
#         print(i)
#         break


# N, K = map(int, input().split())
# A = sorted(list(map(int, input().split())))


# def is_ok(x):
#     cnt = 0
#     for a in A:
#         cnt += (x - 1) // a
#         if cnt >= K:
#             return True
#     return False


# def meguru_bisect(ng, ok):
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if is_ok(mid):
#             ok = mid
#         else:
#             ng = mid
#     return ok


# print(meguru_bisect(0, 10**12))

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(60):
    cnt = 0
    for a in A:
        if a >> i & 1:
            cnt += 1
    ans += cnt * (N - cnt) * (1 << i)

print(ans)
