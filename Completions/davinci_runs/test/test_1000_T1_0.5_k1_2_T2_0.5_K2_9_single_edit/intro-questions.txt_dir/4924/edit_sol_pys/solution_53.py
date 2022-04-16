

import sys
import datetime

def main():
    current_time = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    desired_time = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    current_time = datetime.time(current_time[3], current_time[4], current_time[5])
    desired_time = datetime.time(desired_time[3], desired_time[4], desired_time[5])
    if desired_time < current_time:
        desired_time = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1), desired_time)
    else:
        desired_time = datetime.datetime.combine(datetime.date.today(), desired_time)
    print((desired_time - datetime.datetime.combine(datetime.date.today(), current_time)).total_seconds())

if __name__ == '__main__':
    main()
