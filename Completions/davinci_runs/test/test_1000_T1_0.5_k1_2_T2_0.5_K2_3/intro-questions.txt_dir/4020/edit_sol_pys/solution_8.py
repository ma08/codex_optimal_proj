
import sys

def time_to_minutes(time):
    return time[0] * 60 + time[1] # time[0] is hour and time[1] is minute

def minutes_to_time(minutes):
    return [minutes // 60, minutes % 60] # minutes // 60 is hour, minutes % 60 is minute

def main():
    start_time = [int(x) for x in sys.stdin.readline().split(':')] # split the input by ':'
    end_time = [int(x) for x in sys.stdin.readline().split(':')] # split the input by ':'
    start_minutes = time_to_minutes(start_time)
    end_minutes = time_to_minutes(end_time)
    middle_minutes = (start_minutes + end_minutes) // 2
    middle_time = minutes_to_time(middle_minutes)
    print('{:02d}:{:02d}'.format(middle_time[0], middle_time[1]))

if __name__ == '__main__':
    main()
