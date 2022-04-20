

#import sys
#import math


def main():
    n, d = map(int, input().split())
    points = [list(map(int, input().split())) for _ in range(n)]
    #print(n, d)
    #print(points)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = 0
            for k in range(d):
                dist += (points[i][k] - points[j][k]) ** 2
            if dist ** 0.5 == int(dist ** 0.5):
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()