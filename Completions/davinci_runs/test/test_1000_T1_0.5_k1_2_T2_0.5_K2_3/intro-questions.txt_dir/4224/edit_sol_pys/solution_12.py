

N, K = map(int, input().split())
a = [int(x) for x in input().split()] if N > 0 else []
b = [int(x) for x in input().split()] if K > 0 else []

count = 0

for i in a:
    while i % 2 == 0:
        i /= 2
        count += 1

print(count)
