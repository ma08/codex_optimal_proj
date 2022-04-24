
def distance(point1, point2):
    sum = 0
    for i in range(len(point1)):
        sum += (point1[i] - point2[i])**2
    return sum

def main():
    num_points, dim = map(int, input().split())
    points = []
    for _ in range(num_points):
        points.append(list(map(int, input().split())))
    count = 0
    for i in range(num_points):
        for j in range(i+1, num_points):
            if int(distance(points[i], points[j])**0.5) == distance(points[i], points[j])**0.5:
                count += 1
    print(count)


if __name__ == '__main__':
    main()
