

k = int(input())
n = int(input())

for i in range(n):
    t, z = input().split()
    t = int(t)
    if z == "T":
        k = (k % 8) + 1
    elif z == "N":
        k = k
    elif z == "P":
        k = (k % 8) + 1

print(K)
