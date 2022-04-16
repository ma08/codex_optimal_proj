
n = int(input())
d_list = list(map(int, input().split()))

s = 0
for i in range(n):
    for j in range(i+1, n):
        s += d_list[i] * d_list[j]

print(s)
