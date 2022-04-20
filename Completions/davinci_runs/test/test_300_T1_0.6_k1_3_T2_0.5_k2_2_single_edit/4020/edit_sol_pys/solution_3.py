

def getMidTime(startTime, endTime):
    startMinutes = startTime[0] * 60 + startTime[1]
    endMinutes = endTime[0] * 60 + endTime[1]
    midMinutes = (startMinutes + endMinutes) // 2

    midTime = [0, 0]
    midTime[0] = midMinutes // 60
    midTime[1] = midMinutes % 60

    return midTime

def printTime(time):
    print('{:02d}:{:02d}'.format(time[0],time[1]))

def main():
    startTime = list(map(int, input().split(':')))
    endTime = list(map(int, input().split(':')))

    midTime = getMidTime(startTime, endTime)
    printTime(midTime)

if __name__ == '__main__':
    main()
