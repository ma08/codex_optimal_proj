

def main():
    """main"""
    start_time = input()
    end_time = input()
    start_hour, start_min = start_time.split(':')
    end_hour, end_min = end_time.split(':')
    start_hour = int(start_hour)
    start_min = int(start_min)
    end_hour = int(end_hour)
    end_min = int(end_min)
    if end_hour == start_hour:
        if start_min == 0 and end_min == 0:
            print("{:02d}:{:02d}".format(start_hour, start_min))
        elif start_min == 0 or end_min == 0:
            print("{:02d}:{:02d}".format(start_hour, (start_min+end_min)//2))
        else:
            print("{:02d}:{:02d}".format(start_hour, (start_min+end_min)//2))
    elif end_hour == start_hour+1:
        if start_min == 0 and end_min == 0:
            print("{:02d}:{:02d}".format(start_hour, start_min))
        elif start_min == 0 or end_min == 0:
            print("{:02d}:{:02d}".format(start_hour, (start_min+end_min)//2))
        else:
            print("{:02d}:{:02d}".format(start_hour, (start_min+end_min)//2))
    elif end_hour == start_hour+2:
        if start_min == 0 and end_min == 0:
            print("{:02d}:{:02d}".format(start_hour+1, start_min))
        elif start_min == 0 or end_min == 0:
            print("{:02d}:{:02d}".format(start_hour+1, (start_min+end_min)//2))
        else:
            print("{:02d}:{:02d}".format(start_hour+1, (start_min+end_min)//2))

if __name__ == '__main__':
    main()