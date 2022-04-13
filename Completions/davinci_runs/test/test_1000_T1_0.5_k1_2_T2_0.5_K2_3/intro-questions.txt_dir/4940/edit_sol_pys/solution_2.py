

import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    times = []
    for i in range(N):
        times.append(list(map(int, sys.stdin.readline().split())))
    times = sorted(times, key=lambda x: x[0]) # 按照第一个时间排序
    for i in range(1, M):
        for j in range(N):
            times[j][i] += times[j][i-1]
        times = sorted(times, key=lambda x: x[i]) # 按照第i个时间排序
    print(" ".join(map(str, [times[i][-1] for i in range(N-1)])))

main()
