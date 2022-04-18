
h, v = map(int, input().split())  # h = height, v = angle
print(int(round(h / math.sin(math.radians(v)))))  # round to the nearest integer
