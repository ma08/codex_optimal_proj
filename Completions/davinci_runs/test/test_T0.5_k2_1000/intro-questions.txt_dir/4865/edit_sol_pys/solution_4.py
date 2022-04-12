

from datetime import timedelta

def get_new_time(direction, minutes, hours, minutes_now, seconds_now):
    new_time = timedelta(hours=hours, minutes=minutes_now, seconds=seconds_now) # create new time with current time
    if direction == "F":
        new_time += timedelta(minutes=minutes) # add minutes to new time
    else:
        new_time -= timedelta(minutes=minutes) # subtract minutes from new time
    return new_time

def main():
    num_cases = int(input()) # get number of cases
    for _ in range(num_cases):
        direction, minutes, hours, minutes_now, seconds_now = input().split() # get direction, minutes, hours, minutes_now, seconds_now
        minutes, hours, minutes_now, seconds_now = int(minutes), int(hours), int(minutes_now), int(seconds_now) # convert to int
        new_time = get_new_time(direction, minutes, hours, minutes_now, seconds_now) # get new time
        print(new_time.hour, new_time.minute, new_time.second) # print new time

if __name__ == "__main__":
    main()
