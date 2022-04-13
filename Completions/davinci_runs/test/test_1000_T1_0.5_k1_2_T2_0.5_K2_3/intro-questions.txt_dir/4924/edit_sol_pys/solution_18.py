import sys
import datetime

def main():
    current_time = [int(x) for x in sys.stdin.readline().strip().split(':')]
    desired_time = [int(x) for x in sys.stdin.readline().strip().split(':')]
    current_time = datetime.datetime.now().replace(hour=current_time[0], minute=current_time[1], second=current_time[2])
    desired_time = datetime.datetime.now().replace(hour=desired_time[0], minute=desired_time[1], second=desired_time[2])
    if desired_time < current_time:
        desired_time = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1), desired_time)
    else:
        desired_time = datetime.datetime.combine(datetime.date.today(), desired_time)
    print(desired_time - current_time)

if __name__ == '__main__':
    main()
