

K = int(input())
N = int(input())

for i in range(N):
    T, Z = input().split()
    T = int(T)
    if Z == "T":
        K = (K % 8) + 1
    elif Z == "C":
        K = K % 8
    elif Z == "P":
        K = (K % 8) + 2

print(K)
