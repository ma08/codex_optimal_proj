import sys

def time_to_minutes(hours, minutes):
    return hours * 60 + minutes

def minutes_to_time(hours, minutes):
    return hours // 60, minutes % 60

def main():
    start_time = [int(x) for x in sys.stdin.readline().split(':')]
    end_time = [int(x) for x in sys.stdin.readline().split(':')]
    start_minutes = time_to_minutes(start_time)
    end_minutes = time_to_minutes(end_time)
    middle_minutes = (start_minutes + end_minutes) // 2
    middle_time = minutes_to_time(middle_minutes)
    print('{:02d}:{:02d}'.format(middle_time[0], middle_time[1]))

if __name__ == '__main__':
    main()
