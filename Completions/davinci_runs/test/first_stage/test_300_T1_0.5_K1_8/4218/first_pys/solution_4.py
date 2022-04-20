

N = int(input())
num_odd = 0

for i in range(1, N+1):
    if i % 2 == 1:
        num_odd += 1

print(num_odd / (N+1))