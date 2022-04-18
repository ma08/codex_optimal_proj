
n, c = map(int, input().split())
w = list(map(int, input().split()))
eaten, curr = 0, 0
w.sort()

for x in w:
    if curr + x <= c:
        curr += x
        eaten += 1

print(eaten)
