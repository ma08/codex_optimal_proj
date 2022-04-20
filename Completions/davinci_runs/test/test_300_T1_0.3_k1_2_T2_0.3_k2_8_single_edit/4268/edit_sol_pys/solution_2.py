import math

def main():
    n, d = map(int, input().split())  # n is number of points, d is dimension
    points = []
    for i in range(n):  # input points
        points.append(list(map(int, input().split())))  # points[i] is a list of coordinates
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            distance = 0
            for k in range(d):
                distance += (points[i][k] - points[j][k]) ** 2
            if math.sqrt(distance).is_integer():
                count += 1
    print(count)

if __name__ == '__main__':
    main()
