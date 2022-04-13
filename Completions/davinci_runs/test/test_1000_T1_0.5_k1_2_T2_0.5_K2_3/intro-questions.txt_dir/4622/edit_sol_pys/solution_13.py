n = int(input())
m = int(input())

a_list = [0] * n
for i in range(m):
    l, r = map(int, input().split())
    for j in range(l-1, r):
        a_list[j] = 1

print(sum(a_list))
