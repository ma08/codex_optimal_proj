
n, c = map(int, input().split())
w = list(map(int, input().split()))

eaten = 0
curr = 0
w.sort(reverse=True)

for x in w:
    if curr + x <= c:
        curr += x
        eaten += 1

print(eaten)
