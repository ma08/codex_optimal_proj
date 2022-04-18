

from datetime import datetime
from datetime import timedelta

def get_new_time(direction, minutes, hours, minutes_now, time_now):
    new_time = timedelta(hours=hours, minutes=minutes_now, seconds=time_now.second, microseconds=time_now.microsecond)
    if direction == "F":
        new_time += timedelta(minutes=minutes)
    else:
        new_time -= timedelta(minutes=minutes)
    return new_time

def main():
    num_cases = int(input())
    for _ in range(num_cases):
        direction, minutes, hours, minutes_now = input().split()
        time_now = datetime.now()
        minutes, hours, minutes_now = int(minutes), int(hours), int(minutes_now)
        new_time = get_new_time(direction, minutes, hours, minutes_now, time_now)
        print(new_time.hour, new_time.minute)

if __name__ == "__main__":
    main()
