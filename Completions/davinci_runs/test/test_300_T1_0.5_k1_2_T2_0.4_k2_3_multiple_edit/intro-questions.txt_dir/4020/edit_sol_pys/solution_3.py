import sys

def time_to_minutes(time):
    return time[0] * 60 + time[1]  # noqa

def minutes_to_time(minutes):
    return [minutes // 60, minutes % 60]  # noqa

def main():
    start_time = [int(x) for x in sys.stdin.readline().split(':')]  # noqa
    end_time = [int(x) for x in sys.stdin.readline().split(':')]  # noqa
    start_minutes = time_to_minutes(start_time)  # noqa
    end_minutes = time_to_minutes(end_time)  # noqa
    middle_minutes = (start_minutes + end_minutes) // 2  # noqa
    middle_time = minutes_to_time(middle_minutes)  # noqa
    print('{:02d}:{:02d}'.format(middle_time[0], middle_time[1]))  # noqa

if __name__ == '__main__':
    main()  # noqa
