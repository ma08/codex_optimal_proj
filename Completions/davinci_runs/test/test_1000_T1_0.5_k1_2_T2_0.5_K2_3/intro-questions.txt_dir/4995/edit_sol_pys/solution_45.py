
import sys

def main():
    n = int(sys.stdin.readline().strip())
    total_minutes = 0
    total_seconds = 0
    for i in range(n):
        m, s = map(int, sys.stdin.readline().strip().split())
        total_minutes += m
        total_seconds += s
    avg_min = total_minutes/total_seconds
    if avg_min >= 60:
        print("measurement error")
    else:
        print(avg_min)

if __name__ == "__main__":
    main()
