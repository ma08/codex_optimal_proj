import sys
import datetime

def main():
    current_time = [int(x) for x in sys.stdin.readline().strip().split(':')]
    desired_time = [int(x) for x in sys.stdin.readline().strip().split(':')]
    current_time = datetime.time(current_time[0], current_time[1], current_time[2])
    desired_time = datetime.time(desired_time[0], desired_time[1], desired_time[2])
    if desired_time < current_time:
        desired_time = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1),
                                                 desired_time)
    else:
        desired_time = datetime.datetime.combine(datetime.date.today(), desired_time)
    print(str(desired_time - datetime.datetime.combine(datetime.date.today(),
                                                       current_time)).split('.')[0])

if __name__ == '__main__':
    main()
