

import math

def main():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j: continue
            ans += math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
    print(ans/math.factorial(n))

if __name__ == "__main__":
    main()