

import math

def main():
    N = int(input())
    towns = []
    for i in range(N):
        x, y = map(int, input().split())
        towns.append((x, y))
    sum_lengths = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = towns[i]
            x2, y2 = towns[j]
            sum_lengths += math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print(sum_lengths * 2 / N / (N-1))

if __name__ == '__main__':
    main()