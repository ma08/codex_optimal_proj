

k = int(input())
n = int(input())

for i in range(n):
    t, z = input().split()
    t = int(t)
    k = (t + k) % 8

print(k)
