
import sys
import datetime


def main():
    current_time = [int(x) for x in sys.stdin.readline().strip().split(':')]  # get time in format hh:mm:ss
    desired_time = [int(x) for x in sys.stdin.readline().strip().split(':')]  # get time in format hh:mm:ss
    current_time = datetime.time(current_time[0], current_time[1], current_time[2])  # convert to datetime.time object
    desired_time = datetime.time(desired_time[0], desired_time[1], desired_time[2])  # convert to datetime.time object
    # if desired time is before current time, make it for tomorrow
    if desired_time < current_time:
        desired_time = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1),
                                                 desired_time)  # make datetime.datetime object
    else:
        desired_time = datetime.datetime.combine(datetime.date.today(), desired_time)  # make datetime.datetime object
    print(desired_time - datetime.datetime.combine(datetime.date.today(), current_time))  # print difference


if __name__ == '__main__':
    main()
