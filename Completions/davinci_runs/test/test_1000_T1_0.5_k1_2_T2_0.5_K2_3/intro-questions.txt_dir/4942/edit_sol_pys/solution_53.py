
import sys

def main():
    num_soldiers = int(sys.stdin.readline().strip())
    soldier_growth_times = [int(x) for x in sys.stdin.readline().strip().split()]
    soldier_growth_times.sort()
    max_time = soldier_growth_times[-1]
    for i in range(len(soldier_growth_times)-2, -1, -1):
        max_time += 1 + soldier_growth_times[i]
    print(max_time)

if __name__ == '__main__':
    main()
