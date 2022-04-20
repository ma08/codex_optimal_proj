

n = int(input())
v = list(map(int, input().split()))

v.sort()

while len(v) > 1:
    v.append((v.pop(0) + v.pop(0)) / 2)
    v.sort()

print(v[0])