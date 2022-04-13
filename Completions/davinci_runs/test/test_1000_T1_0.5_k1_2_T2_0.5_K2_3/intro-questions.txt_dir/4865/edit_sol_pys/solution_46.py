

from datetime import timedelta

def get_new_time(direction, minutes, hours, minutes_now, hours_now):
    new_time = timedelta(hours=hours_now, minutes=minutes_now, seconds=0)
    if direction == "F":
        new_time += timedelta(minutes=minutes, seconds=0)
    else:
        new_time -= timedelta(minutes=minutes, seconds=0)
    return new_time

def main():
    num_cases = int(input())
    for _ in range(num_cases):
        direction, minutes, hours, minutes_now, hours_now = input().split() #read input
        minutes, hours, minutes_now, hours_now = int(minutes), int(hours), int(minutes_now), int(hours_now) #convert to int
        new_time = get_new_time(direction, minutes, hours, minutes_now, hours_now)
        print(new_time.hour, new_time.minute)

if __name__ == "__main__":
    main()
