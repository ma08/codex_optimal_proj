

from datetime import timedelta, datetime

def get_new_time(direction, minutes, hours, minutes_now, hours_now):
    new_time = timedelta(hours=hours_now, minutes=minutes_now)
    if direction == "F":
        new_time += timedelta(minutes=minutes)
    else:
        new_time -= timedelta(minutes=minutes)
    return new_time

def main():
    direction, minutes, hours, minutes_now, hours_now = input().split()
    minutes, hours, minutes_now, hours_now = int(minutes), int(hours), int(minutes_now), int(hours_now)
    new_time = get_new_time(direction, minutes, hours, minutes_now, hours_now)
    print(new_time.hour, new_time.minute)

if __name__ == "__main__":
    main()
