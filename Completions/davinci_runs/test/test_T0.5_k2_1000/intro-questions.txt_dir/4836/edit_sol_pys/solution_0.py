n, c = map(int, input().split())
w = list(map(int, input().split()))
w.sort()

eaten = 1
curr = w[0]

for x in w[1:]:
    if curr + x <= c:
        curr += x
        eaten += 1

print(eaten)
