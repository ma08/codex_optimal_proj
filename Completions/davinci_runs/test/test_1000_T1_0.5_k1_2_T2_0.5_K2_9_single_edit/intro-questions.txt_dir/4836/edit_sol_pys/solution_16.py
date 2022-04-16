

n, c = map(int, input().split())
w = list(map(int, input().split()))

eaten = 0
curr = 0
w.sort()

for i in w:
    if curr + i <= c:
        curr += i
        eaten += 1

print(eaten)
