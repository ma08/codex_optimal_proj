#!/usr/bin/python3

import sys

def main():
    num_seedlings = int(sys.stdin.readline())
    seedling_growth_times = [int(x) for x in sys.stdin.readline().split()]
    seedling_growth_times.sort()
    max_time = seedling_growth_times[-1]
    for i in range(len(seedling_growth_times)-2,-1,-1):
        max_time += 1 + seedling_growth_times[i]
    print(max_time, end='')

if __name__ == '__main__':
    main()
