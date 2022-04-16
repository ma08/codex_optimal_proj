

K = int(input())
N = int(input())

for i in range(1, N + 1):
    T, Z = input().split()    
    if Z == "T" and i % 2 == 0:
        K = (K % 8) + 1
    elif Z == "N" and i % 2 == 1:
        K = (K % 8) + 1
    elif Z == "P" and i % 2 == 0:
        K = (K % 8) + 1
    elif Z == "P" and i % 2 == 1:
        K = K 

print(K)
