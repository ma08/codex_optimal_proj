

# NOTE: I didn't know how to do this without using python's datetime module, so I just used it. It's not very efficient, but it gets the job done.

import datetime

def main():
    num_cases = int(input())
    for i in range(num_cases):
        case = input().split()
        direction = case[0]
        minutes = int(case[1])
        hour = int(case[2])
        minute = int(case[3])
        if direction == 'B':
            minutes *= -1
        time = datetime.datetime(1, 1, 1, hour, minute) + datetime.timedelta(minutes=minutes)
        print('{} {}'.format(time.hour, time.minute))

main()
