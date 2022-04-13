
import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    times = []
    for i in range(N):
        times.append(list(map(int, sys.stdin.readline().split())))
    times = sorted(times, key=lambda x: x[0]) # sort by time
    for i in range(1, M):
        for j in range(N):
            times[j][i] += times[j][i-1]
        times = sorted(times, key=lambda x: x[i]) # sort by order
    print(" ".join(map(str, [times[i][-1] for i in range(N)])))

main()
