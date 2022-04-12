

import sys
import datetime

def main():
    current_time = [int(x) for x in input().strip().split(':')] # split the input by :
    desired_time = [int(x) for x in input().strip().split(':')] # split the input by :
    current_time = datetime.datetime(2000, 1, 1, current_time[0], current_time[1], current_time[2])
    desired_time = datetime.datetime(2000, 1, 1, desired_time[0], desired_time[1], desired_time[2])
    if desired_time <= current_time: # if the desired time is less than or equal to the current time
        desired_time += datetime.timedelta(days=1)
    else:
        pass
    print(desired_time - current_time)

if __name__ == '__main__':
    main()
