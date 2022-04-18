import collections

n, x = map(int, input().split())
q = int(input())
query_list = [input().split() for _ in range(q)]
l_list = list(map(int, input().split()))

coord_list = [0] * (n + 1)

for i in range(1, n + 1):
    coord_list[i] = coord_list[i - 1] + l_list[i - 1]

print(len(list(filter(lambda x: x <= x, coord_list))))
