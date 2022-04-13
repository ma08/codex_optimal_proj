
K = int(input())
N = int(input())

for i in range(N):
    T, Z = input().split()
    T = int(T)
    if Z == "T":
        K = (K % 8) + 1

print(K)
