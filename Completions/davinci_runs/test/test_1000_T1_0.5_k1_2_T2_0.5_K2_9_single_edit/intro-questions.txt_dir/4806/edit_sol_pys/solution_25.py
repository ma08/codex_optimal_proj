
import sys
def main():
    num_cases = int(sys.stdin.readline().strip())
    for _ in range(num_cases):
        num_days = int(sys.stdin.readline().strip())
        day_counts = [0] * num_days
        num_groups = int(sys.stdin.readline().strip())
        for _ in range(num_groups):
            start_day, duration = sys.stdin.readline().strip().split()
            start_day, duration = int(start_day), int(duration)
            for i in range(start_day, start_day + duration):
                day_counts[i] += 1
        print(max(day_counts))

if __name__ == '__main__':
    main()
