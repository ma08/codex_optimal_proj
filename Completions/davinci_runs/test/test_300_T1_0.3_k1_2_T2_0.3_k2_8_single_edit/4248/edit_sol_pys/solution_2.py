
import math

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append([float(x) for x in input().split()])

    angles = []
    for i in range(n):
        for j in range(i + 1, n):
            angle = math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0]) % (2 * math.pi)
            angles.append(angle)

    angles.sort()
    angles.append(angles[0] + 2 * math.pi) # for the case where the largest angle is between the first and last points

    max_angle = 0
    for i in range(n):
        angle = angles[i + 1] - angles[i]
        if angle > max_angle:
            max_angle = angle

    print(math.degrees(max_angle))

if __name__ == "__main__":
    main()
