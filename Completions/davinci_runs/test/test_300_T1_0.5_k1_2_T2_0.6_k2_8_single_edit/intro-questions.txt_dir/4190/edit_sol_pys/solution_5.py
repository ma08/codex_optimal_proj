
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [0] * n
for i in range(n):
    c[(a[i] + b[i]) % n] += 1

for i in range(n):
    for j in range(c[i] - 1):
        print(i, end=" ")  # print the number of times the modulo occurs
