

import sys

def main():
    n = int(sys.stdin.readline().strip())
    max_speed = 0
    prev_time = 0
    prev_dist = 0
    for i in range(n):
        time, distance = map(int, sys.stdin.readline().strip().split())
        speed = (distance - prev_dist) / float(time - prev_time)
        if speed > max_speed:
            max_speed = speed
        prev_time, prev_dist = time, distance
    print(int(max_speed))
    
if __name__ == "__main__":
    main()
