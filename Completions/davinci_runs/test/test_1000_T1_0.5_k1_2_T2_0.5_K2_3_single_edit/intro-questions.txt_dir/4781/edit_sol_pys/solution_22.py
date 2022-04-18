

K = int(input())
N = int(input())

for i in range(N):
    T, Z = input().split()
    T = int(T)
    if Z == "T":
        K = (K % 8) + T
    elif Z == "N":
        K = K + T
    elif Z == "P":
        K = (K % 8) + T

print(K)
