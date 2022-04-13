

import sys

def main():
    n = int(sys.stdin.readline().strip())
    total_minutes = 0
    total_seconds = 0
    for i in range(n):
        m, s = map(int, sys.stdin.readline().strip().split())
        total_minutes += m
        total_seconds += s
    avg_sec = total_seconds/total_minutes if total_minutes != 0 else 0
    if avg_sec <= 60:
        print("measurement error")
    else:
        print(avg_sec)

if __name__ == "__main__":
    main()
