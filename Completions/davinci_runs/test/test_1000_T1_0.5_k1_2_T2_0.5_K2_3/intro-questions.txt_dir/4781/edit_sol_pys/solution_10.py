
K = int(input())
N = int(input())
for i in range(N):
    T, Z = input().split()
    T = int(T)
    if Z == "T":
        K = (K + 1) % 8
    elif Z == "N":
        K = K
    elif Z == "P":
        K = (K - 1) % 8

print(K)
