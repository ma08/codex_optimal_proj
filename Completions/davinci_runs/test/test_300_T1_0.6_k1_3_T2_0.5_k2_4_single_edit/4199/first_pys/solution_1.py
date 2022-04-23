

N, K = map(int, input().split())
h = list(map(int, input().split()))

print(len([x for x in h if x >= K]))
"""
N, K = map(int, input().split())
h = list(map(int, input().split()))

count = 0
for x in h:
    if x >= K:
        count += 1
print(count)
"""