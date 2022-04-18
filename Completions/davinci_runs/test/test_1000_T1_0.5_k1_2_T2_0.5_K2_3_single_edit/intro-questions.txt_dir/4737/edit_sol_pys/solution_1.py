

import sys

def main():
    N, p = map(int, sys.stdin.readline().split())
    times = map(int, sys.stdin.readline().split())
    # print(N, p)
    # print(times)
    # print('')
    best = [0, 0, 0]
    for i in range(N):
        if i == p:
            continue
        # print('i:', i)
        # print('times[i]:', times[i])
        # print('times[p]:', times[p])
        # print('times[i] + times[p]:', times[i] + times[p])
        # print('times[i] + times[p] < 300:', times[i] + times[p] < 300)
        if times[i] + times[p] < 300:
            # print('best[0]:', best[0])
            # print('best[1]:', best[1])
            # print('times[i]:', times[i])
            # print('times[p]:', times[p])
            # print('times[i] + times[p]:', times[i] + times[p])
            if times[i] + times[p] < best[1]:
                best[0] = i
                best[1] = times[i] + times[p]
                best[2] = times[i]
        else:
            if times[p] < best[1]:
                best[0] = i
                best[1] = times[i] + times[p]
                best[2] = times[p]
    # print(best)
    print(best[0] + 1, best[2])

main()
