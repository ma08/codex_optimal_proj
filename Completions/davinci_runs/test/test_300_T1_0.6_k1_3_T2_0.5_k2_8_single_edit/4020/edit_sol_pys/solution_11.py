

def getMidTime(startTime, endTime):
    start_minutes = startTime[1] + (startTime[0] * 60)
    end_minutes = endTime[1] + (endTime[0] * 60)
    mid_minutes = start_minutes + (end_minutes - start_minutes) / 2


    mid_time = [0, 0]
    mid_time[0] = mid_minutes / 60
    mid_time[1] = mid_minutes % 60

    return mid_time

def print_time(time):
    print('{:02d}:{:02d}'.format(time[0], time[1]))

def main():
    startTime = list(map(int, input().split(':')))
    endTime = list(map(int, input().split(':')))

    mid_time = getMidTime(startTime, endTime)
    print_time(mid_time)

if __name__ == '__main__':
    main()
