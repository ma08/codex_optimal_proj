

k = int(input())
n = int(input())
for i in range(n):
    t, z = input().split()
    t = int(t)
    if t > 210:
        break
    if z == "T":
        k = (k + 1) % 8
    if z == "N":
    if k < 1:
        k = 8
        k = (k - 1) % 8
print(k)
