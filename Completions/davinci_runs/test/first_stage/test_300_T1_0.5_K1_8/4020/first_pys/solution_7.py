


def find_midpoint(start_hour, start_minute, end_hour, end_minute):
    start_time = start_hour * 60 + start_minute
    end_time = end_hour * 60 + end_minute
    midpoint = (start_time + end_time) / 2
    if midpoint % 2 == 1:
        midpoint += 1
    mid_hour = midpoint / 60
    mid_minute = midpoint % 60
    return mid_hour, mid_minute


def main():
    start_hour, start_minute = map(int, raw_input().split(':'))
    end_hour, end_minute = map(int, raw_input().split(':'))
    mid_hour, mid_minute = find_midpoint(start_hour, start_minute, end_hour, end_minute)
    print '%02d:%02d' % (mid_hour, mid_minute)


if __name__ == '__main__':
    main()