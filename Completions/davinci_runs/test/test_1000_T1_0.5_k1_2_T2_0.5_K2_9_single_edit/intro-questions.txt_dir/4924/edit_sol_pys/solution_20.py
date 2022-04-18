

import sys
import datetime

def main():
    current_time = [int(x) for x in sys.stdin.readline().strip().split(':')]
    desired_time = [int(x) for x in sys.stdin.readline().strip().split(':')]
    c_time = datetime.time(current_time[0], current_time[1], current_time[2])
    d_time = datetime.time(desired_time[0], desired_time[1], desired_time[2])
    if d_time < c_time:
        d_time = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1), d_time)
    else:
        d_time = datetime.datetime.combine(datetime.date.today(), d_time)
    print(d_time - datetime.datetime.combine(datetime.date.today(), c_time))

if __name__ == '__main__':
    main()
