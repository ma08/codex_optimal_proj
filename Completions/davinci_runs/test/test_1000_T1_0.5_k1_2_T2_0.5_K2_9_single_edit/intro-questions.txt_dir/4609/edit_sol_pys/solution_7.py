

n = int(input())
a = [0] * 1000000
for i in range(n):
    a[int(input())] += 1

print(sum(map(lambda x: x % 2, a)))
