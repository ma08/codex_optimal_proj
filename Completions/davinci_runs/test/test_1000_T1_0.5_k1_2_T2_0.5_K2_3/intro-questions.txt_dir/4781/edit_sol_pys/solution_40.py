
K = int(input())
N = int(input())

for i in range(N):
    t, z = input().split()
    t = int(t)
    if z == "T":
        K = (K % 8) + 1
    elif z == "F":
        K = (K % 8) + 1

print(K)
