

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
        time = datetime.datetime(1, 1, 1, hour, minute)
        time += datetime.timedelta(minutes=minutes)
        print('{} {}'.format(time.hour, time.minute))

main()
