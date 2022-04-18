
N = int(input())
p = list(map(int, input().split()))

p_sorted = sorted(p)  # 配列pを昇順にソートした配列

# p_sortedの要素がpに全て存在するか
if all(p_sorted[i] in p for i in range(N)):
    print("YES")
else:
    print("NO")


# for i in range(N):
#     if p[i] == p_sorted[i]:
#         continue
#     else:
#         p[i], p[p.index(p_sorted[i])] = p[p.index(p_sorted[i])], p[i]
#         if p == p_sorted:
#             print("YES")
#             exit()

# print("NO")
