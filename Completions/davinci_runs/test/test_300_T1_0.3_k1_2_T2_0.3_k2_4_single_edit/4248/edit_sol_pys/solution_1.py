
import math

def main():
    n = int(input("Enter number of points: "))
    points = []
    for i in range(n):
        points.append([float(x) for x in input("Enter the coordinates of point {}: ".format(i + 1)).split()])

    angles = []
    for i in range(n):
        for j in range(i + 1, n):
            angle = math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])
            angles.append(angle)

    angles.sort()
    angles.append(angles[0] + 2 * math.pi)

    max_angle = 0
    for i in range(n):
        angle = angles[i + 1] - angles[i]
        if angle > max_angle:
            max_angle = angle

    print("The maximum angle is {} degrees".format(math.degrees(max_angle)))

if __name__ == "__main__":
    main()
