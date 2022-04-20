

def getMidTime(startTime, endTime):
    startMinutes = startTime[1] + (startTime[0] * 60)  # convert to minutes
    endMinutes = endTime[1] + (endTime[0] * 60)  # convert to minutes
    midMinutes = startMinutes + (endMinutes - startMinutes) / 2  # get mid time

    midTime = [0, 0]
    midTime[0] = int(midMinutes / 60)  # convert to hours
    midTime[1] = int(midMinutes % 60)  # convert to minutes

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
