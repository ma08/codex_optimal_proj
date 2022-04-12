

h, v = map(int, input().split())
print(int(round(h / math.sin(math.radians(v)))))
