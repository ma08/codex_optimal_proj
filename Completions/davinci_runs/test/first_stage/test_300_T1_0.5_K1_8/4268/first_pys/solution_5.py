

import sys
import math

def main():
    n, d = map(int, input().split())
    points = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = sum(map(lambda x: (x[0]-x[1])**2, zip(points[i], points[j])))
            if math.sqrt(dist).is_integer():
                count += 1
    print(count)

if __name__ == '__main__':
    main()