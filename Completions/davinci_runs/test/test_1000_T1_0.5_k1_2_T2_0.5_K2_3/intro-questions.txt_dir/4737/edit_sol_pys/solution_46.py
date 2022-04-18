
import sys

def main():
    N, p = map(int, input().split())
    times = map(int, input().split())

    best = [0, 0]
    for i in range(N):
        if i == p:
            continue

        if times[i] + times[p] < 300:

            if best[0] == 0 or times[i] + times[p] < best[1]:
                best = [2, times[i] + times[p]]
        else:
            if best[0] == 0 or times[p] < best[1]:
                best = [1, times[p]]

    print(*best)

main()
