

import sys

def main():
    N, p = map(int, sys.stdin.readline().split()) # N = number of students, p = position of student in line
    times = map(int, sys.stdin.readline().split()) # times = times it takes each student to print in minutes
    # print(N, p)
    # print(times)
    # print('')
    best = [0, 0] # best = [number of students, time in minutes]
    for i in range(N):
        if i == p: # skip the student in position p
            continue
        # print('i:', i)
        # print('times[i]:', times[i])
        # print('times[p]:', times[p])
        # print('times[i] + times[p]:', times[i] + times[p])
        # print('times[i] + times[p] < 300:', times[i] + times[p] < 300)
        if times[i] + times[p] < 300: # if the total time is less than 5 minutes
            # print('best[0]:', best[0])
            # print('best[1]:', best[1])
            # print('times[i]:', times[i])
            # print('times[p]:', times[p])
            # print('times[i] + times[p]:', times[i] + times[p])
            if best[0] == 0: # if this is the first time through
                best[0] = 2
                best[1] = times[i] + times[p]
            elif times[i] + times[p] < best[1]: # if this is a better time than the current best
                best[0] = 2
                best[1] = times[i] + times[p]
        else: # if the total time is more than 5 minutes
            if best[0] == 0: # if this is the first time through
                best[0] = 1
                best[1] = times[p]
            elif times[p] < best[1]: # if this is a better time than the current best
                best[0] = 1
                best[1] = times[p]
    # print(best)
    print(best[0], best[1])

main()
