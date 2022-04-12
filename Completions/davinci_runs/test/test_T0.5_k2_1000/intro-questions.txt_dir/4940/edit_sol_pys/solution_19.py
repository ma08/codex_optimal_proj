
import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    times = []
    for i in range(N):
        times.append(list(map(int, sys.stdin.readline().split())))
    times = sorted(times, key=lambda x: x[0]) # sort by first column
    for i in range(1, M): # for each column
        for j in range(N): # for each row
            times[j][i] += times[j][i-1] # add previous column to current column
        times = sorted(times, key=lambda x: x[i]) # sort by current column
    print(" ".join(map(str, [times[i][-1] for i in range(N)]))) # print last column

main()
