

lines = []
for i in range(3):
    lines.append(input())

def get_coords(line):
    coords = line.split()
    return (int(coords[0]), int(coords[1]))

points = []
for line in lines:
    points.append(get_coords(line))

if points[0][0] == points[1][0]:
    x = points[2][0] if points[0][0] == points[2][0] else points[1][0]
else:
    x = points[0][0]

if points[0][1] == points[1][1]:
    y = points[2][1] if points[0][1] == points[2][1] else points[1][1]
else:
    y = points[0][1]

print(x, y)
