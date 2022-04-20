
import math

def main():
    t = int(input())
    for i in range(t):
        n, d = map(int, input().split())
        points = []
        for j in range(n):
            points.append(list(map(int, input().split())))
        count = 0
        for j in range(n):
            for k in range(j+1, n):
                distance = 0
                for l in range(d):
                    distance += (points[j][l] - points[k][l]) ** 2
                if math.sqrt(distance).is_integer():
                    count += 1
        print(count)

if __name__ == '__main__':
    main()
