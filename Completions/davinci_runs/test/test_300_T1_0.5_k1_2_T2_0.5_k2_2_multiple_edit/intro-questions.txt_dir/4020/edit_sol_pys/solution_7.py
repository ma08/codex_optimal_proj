
import sys

def time_to_minutes(time):
    return time[0]*60+time[1]

def minutes_to_time(minutes):
    return [minutes//60, minutes%60]

def main():
    startTime = [int(x) for x in sys.stdin.readline().split(':')]
    endTime = [int(x) for x in sys.stdin.readline().split(':')]
    startMinutes = time_to_minutes(startTime)
    endMinutes = time_to_minutes(endTime)
    middleMinutes = (startMinutes+endMinutes)//2
    middleTime = minutes_to_time(middleMinutes)
    print('{:02d}:{:02d}'.format(middleTime[0],middleTime[1]))

if __name__ == '__main__':
    main()
