input = sys.stdin.readline
n, m, x = map(int, input().split())
a_list = list(map(int, input().split()))

cost = 0
for i in range(x, 0, -1):
    if i in a_list:
        cost += 1

for i in range(x, n + 1):
    if i in a_list:
        cost += 1

print(cost)
