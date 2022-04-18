
import sys

def main():
    num_seedlings = int(sys.stdin.readline().strip())
    seedling_growth_times = [int(x) for x in sys.stdin.readline().strip().split()]
    seedling_growth_times.sort()
    max_time = seedling_growth_times[0]
    for i in range(1,len(seedling_growth_times)):
        max_time += 1 + seedling_growth_times[i]
    print(max_time)

if __name__ == '__main__':
    main()
