#
# N = int(input())
#
# start = []
# end = []
#
# for i in range(N):
#     s, t = map(int, input().split())
#     start.append(s)
#     end.append(t)
#
# start.sort()
# end.sort()
# total = 0
# i = 0
# j = 0
# while i < N:
#     if start[i] <= end[j]:
#         total += start[i] - end[j] + 1
#         i += 1
#     else:
#         j += 1
#
# print(total)
