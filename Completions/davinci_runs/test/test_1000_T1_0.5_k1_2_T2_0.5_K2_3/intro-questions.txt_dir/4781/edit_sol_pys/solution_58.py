
# 简单题，模拟就可以了

k = int(input()) 
n = int(input())
for i in range(n):
    t, z = input().split()
    t = int(t)
    if t > 210:
        break
    if z == "T":
        k = (k + 1) % 8
    else:
        k = (k - 1) % 8
print(k)
