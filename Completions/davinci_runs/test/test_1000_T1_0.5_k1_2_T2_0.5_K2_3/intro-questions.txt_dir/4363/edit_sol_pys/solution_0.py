
K, S = map(int, input().split())

count = 0

for x in range(K+1):
    for y in range(K+1):
        for z in range(K+1):
            if x + y + z == S:
                count += 1
print(count)
