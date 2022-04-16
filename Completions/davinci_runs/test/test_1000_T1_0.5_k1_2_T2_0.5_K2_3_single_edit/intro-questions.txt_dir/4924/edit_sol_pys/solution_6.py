import datetime

import sys

def main():
    current_time = datetime.datetime.strptime(sys.stdin.readline().strip(), '%H:%M:%S')
    desired_time = datetime.datetime.strptime(sys.stdin.readline().strip(), '%H:%M:%S')
    if desired_time < current_time:
        desired_time += datetime.timedelta(days=1)
    print(desired_time - current_time)

if __name__ == '__main__':
    main()
