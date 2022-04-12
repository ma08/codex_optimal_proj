
import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    times = []
    for i in range(N):
        times.append(list(map(int, sys.stdin.readline().split())))
    times = sorted(times, key=lambda x: x[0])
    for i in range(1, M): # i는 시간
        for j in range(N):
            times[j][i] += times[j][i-1]
        times = sorted(times, key=lambda x: x[i]) # i번째 시간에 도착하는 순서대로 정렬
    print(" ".join(map(str, [times[i][-1] for i in range(N)])))

main()
