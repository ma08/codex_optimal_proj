

N = int(input())
a = [int(x) for x in input().split()]
count = 0

for i in a:
    while i % 2 == 0 and i != 0:
        i //= 2
        count += 1

print(count)
