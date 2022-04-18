

n, x = map(int, input().split())
l_list = list(map(int, input().split()))

coord_list = [0]

for i in range(n):
    coord_list.append(coord_list[i] + l_list[i])
print(len(list(filter(lambda x: x <= x, coord_list)))) 
