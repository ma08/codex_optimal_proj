K = int(input())
N = int(input())
for i in range(N):
    T, Z = input().split(" ")
    T = int(T)
    if Z == "T":
        K = (K % 8) + 1 if K < 8 else 1
    elif Z == "N":
        K = K
    elif Z == "P":
        K = (K % 8) + 1 if K < 8 else 1

print(K)
