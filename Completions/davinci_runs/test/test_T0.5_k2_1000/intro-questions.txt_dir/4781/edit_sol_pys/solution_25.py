
k = int(input())
n = int(input())
for i in range(n):
    t, z = input().split()
    t = int(t)
    if t > 210:
        break
    if z == "T":
        k = (k + 1) % 8
    elif z == "N":
        k = (k - 1) % 8
print(k)
