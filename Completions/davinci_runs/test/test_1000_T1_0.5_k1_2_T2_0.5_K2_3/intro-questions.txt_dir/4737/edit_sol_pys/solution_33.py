

import sys

def main():
    N, p = map(int, sys.stdin.readline().split())
    times = list(map(int, sys.stdin.readline().split()))

    best = [0, 0]
    for i in range(N):
        if i == p:
            continue

        if times[i] + times[p] < 300:

            if best[0] == 0:
                best[0] = 2
                best[1] = times[i] + times[p]
            elif times[i] + times[p] < best[1]:
                best[0] = 2
                best[1] = times[i] + times[p]
        else:
            if best[0] == 0:
                best[0] = 1
                best[1] = times[p]
            elif times[p] < best[1]:
                best[0] = 1
                best[1] = times[p]
    print(best[0], best[1])

main()
