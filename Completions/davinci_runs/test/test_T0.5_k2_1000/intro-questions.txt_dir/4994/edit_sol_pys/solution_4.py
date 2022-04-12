
lines = []
for i in range(3):
    lines.append(input())

def get_coords(line):
    coords = line.split()
    return [int(coords[0]), int(coords[1])]

points = []
for line in lines:
    points.append(get_coords(line))

if points[0][0] == points[1][0] and points[0][0] != points[2][0]:
    x = points[2][0]
elif points[0][0] == points[2][0] and points[0][0] != points[1][0]:
    x = points[0][0]
elif points[1][0] == points[2][0] and points[1][0] != points[0][0]:
    x = points[0][0]

if points[0][1] == points[1][1] and points[0][1] != points[2][1]:
    y = points[2][1]
elif points[0][1] == points[2][1] and points[0][1] != points[1][1]:
    y = points[0][1]
elif points[1][1] == points[2][1] and points[1][1] != points[0][1]:
    y = points[0][1]

print(x, y)
