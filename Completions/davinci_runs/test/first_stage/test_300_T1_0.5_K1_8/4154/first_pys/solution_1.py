

input_data = input().split()
n = int(input_data[0])
m = int(input_data[1])
l_r_list = []
for i in range(m):
    l_r_list.append(input().split())

l_r_list.sort(key=lambda x: int(x[1]))

last_r = 0
ans = 0
for i in range(m):
    if int(l_r_list[i][0]) > last_r:
        last_r = int(l_r_list[i][1])
        ans += 1

print(ans)