

def main():
    n, d = map(int, input().strip().split())
    points = []
    for _ in range(n):
        points.append(list(map(int, input().strip().split())))

    result = 0
    for i in range(n):
        for j in range(i+1, n):
            distance = 0
            for k in range(d):
                distance += (points[i][k] - points[j][k])**2
            if distance ** 0.5 == int(distance ** 0.5):
                result += 1
    print(result)


if __name__ == '__main__':
    main()