N = int(input())
a = [int(x) for x in input().split()]

count = 0

for i in range(N):
    while i % 2 == 0:
        i /= 2
        count += 1

print(count)
