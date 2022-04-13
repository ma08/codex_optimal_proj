import sys

from datetime import timedelta

def get_new_time(direction, minutes, hours, minutes_now, hours_now):
    new_time = timedelta(hours=hours_now, minutes=minutes_now)
    if direction == "F":
        new_time += timedelta(minutes=minutes)
    else:
        new_time -= timedelta(minutes=minutes)
    return new_time

def main():
    num_cases = int(sys.stdin.readline())
    for _ in range(num_cases):
        direction, minutes, hours, minutes_now, hours_now = sys.stdin.readline().split()
        minutes, hours, minutes_now, hours_now = int(minutes), int(hours), int(minutes_now), int(hours_now)
        new_time = get_new_time(direction, minutes, hours, minutes_now, hours_now)
        print(new_time.hour, new_time.minute)

if __name__ == "__main__":
    main()
