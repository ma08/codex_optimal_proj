
n = int(input())
a = [int(x) for x in input().split()]

count = 0
while all(x % 2 == 0 for x in a) and len(a) > 0:
    a = [x // 2 for x in a]
    count += 1

print(count)
