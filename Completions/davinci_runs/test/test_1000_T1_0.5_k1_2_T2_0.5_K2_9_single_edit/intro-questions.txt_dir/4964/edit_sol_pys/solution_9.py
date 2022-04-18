# # Solution
# def solve():
#     N, H, L = map(int, input().split())
#     horror_list = set(map(int, input().split()))
#     similarities = [list(map(int, input().split())) for _ in range(L)]
#     HI = [0] * N
#     for i in range(N):
#         if i in horror_list:
#             HI[i] = 0
#         else:
#             HI[i] = float('inf')
#     for a, b in similarities:
#         if HI[a] < HI[b]:
#             HI[b] = HI[a] + 1
#         elif HI[b] < HI[a]:
#             HI[a] = HI[b] + 1
#     print(HI.index(max(HI)))

# Solution
def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if a[j][i] == 1:
                for k in range(n):
                    if a[k][i] == 1 and k != j:
                        a[k][i] = 0
    ans = 0
    for i in range(n):
        if sum(a[i]) == 0:
            ans += 1
    print(ans)

solve()
