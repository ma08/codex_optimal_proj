import sys

def time_to_minutes(time):
    return time[0] * 60 + time[1]

def minutes_to_time(minutes):
    return [minutes // 60, minutes % 60]

def main():
    start_time = sys.stdin.readline().split(':')
    end_time = sys.stdin.readline().split(':')
    start_minutes = int(start_time[0]) * 60 + int(start_time[1])
    end_minutes = int(end_time[0]) * 60 + int(end_time[1])
    middle_minutes = (start_minutes + end_minutes) // 2 - 60
    print('{:02d}:{:02d}'.format(middle_minutes // 60, middle_minutes % 60))

if __name__ == '__main__':
    main()
