

#-------------------------------------------------------------------------------

n, V = map(int, input().split()) # n = number of boxes, V = volume of the box
volumes = []
for _ in range(n):
    l, w, h = map(int, input().split())
    volumes.append(l * w * h)

print(max(volumes) - V)
