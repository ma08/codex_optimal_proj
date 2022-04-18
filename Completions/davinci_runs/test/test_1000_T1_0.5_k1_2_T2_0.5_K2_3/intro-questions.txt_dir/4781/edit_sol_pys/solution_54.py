
K = int(input())
N = int(input())

for i in range(N):
    t, z = input().split()
    t = int(t)
    K = (t + K) % 8

print(K)
