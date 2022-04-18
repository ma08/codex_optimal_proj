
n, m, x = map(int, input().split())
a_list = list(map(int, input().split()))

left_cost = 0
right_cost = 0
for i in range(x, -1, -1):
    if i in a_list: left_cost += 1

for i in range(x, n + 1):
    if i in a_list: right_cost += 1

print(min(left_cost, right_cost))
