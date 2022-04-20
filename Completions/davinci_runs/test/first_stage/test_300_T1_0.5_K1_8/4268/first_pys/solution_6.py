
import itertools
import math

def get_strings():
    N, D = map(int, input().split(" "))
    points = []
    for i in range(N):
        points.append(list(map(int, input().split(" "))))
    return N, D, points

def main():
    N, D, points = get_strings()
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            dist = 0
            for k in range(D):
                dist += (points[i][k] - points[j][k]) ** 2
            dist = math.sqrt(dist)
            if dist == int(dist):
                count += 1
    print(count)

if __name__ == '__main__':
    main()