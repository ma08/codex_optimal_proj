n, l = map(int, input().split())
flavours = [l + i for i in range(n)]

print(sum(flavours) - min([abs(f) for f in flavours]))
