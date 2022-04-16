
K = int(input())
N = int(input())

for i in range(N):
    T, D = input().split()
    T = int(T) % 8
    if D == "T":
        K = T
    elif D == "N":
        K = K % 8
    elif D == "P":
        K = (K % 8) + T

print(K)
