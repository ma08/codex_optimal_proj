
import sys

def time_to_minutes(time):
    return time[0] * 60 + time[1]

def minutes_to_time(minutes):
    return [minutes // 60, minutes % 60]

def main():
    start_time = [int(x) for x in sys.stdin.readline().split()]
    end_time = [int(x) for x in sys.stdin.readline().split()]
    start_minutes = time_to_minutes(start_time) # convert start time to minutes
    end_minutes = time_to_minutes(end_time) # convert end time to minutes
    middle_minutes = (start_minutes + end_minutes) // 2 # calculate middle time in minutes
    middle_time = minutes_to_time(middle_minutes) # convert middle time to time
    print('{:02d}:{:02d}'.format(middle_time[0], middle_time[1])) # print middle time

if __name__ == '__main__':
    main()
