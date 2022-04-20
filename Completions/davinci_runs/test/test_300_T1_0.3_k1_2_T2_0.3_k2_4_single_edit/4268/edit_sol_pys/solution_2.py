
import sys

def main():
    N, D = map(int, sys.stdin.readline().strip().split())
    points = []
    for i in range(N):
        points.append(list(map(int, sys.stdin.readline().strip().split())))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = 0
            for k in range(D):
                dist += (points[i][k] - points[j][k])**2
            if dist**0.5 == int(dist**0.5):
                count += 1
    print(count)

if __name__ == '__main__':
    main()
