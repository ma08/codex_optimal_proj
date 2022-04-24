

n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

ans = 0

for i in range(n):
    coord_list.append(coord_list[i] + l_list[i])

print(len(list(filter(lambda x: x <= x, coord_list))))
