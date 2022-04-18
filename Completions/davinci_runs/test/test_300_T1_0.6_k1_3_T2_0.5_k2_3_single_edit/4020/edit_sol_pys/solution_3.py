

def getMidTime(startTimeHours, startTimeMinutes, endTimeHours, endTimeMinutes):
    startMinutes = startTimeMinutes + (startTimeHours * 60)
    endMinutes = endTimeMinutes + (endTimeHours * 60)
    midMinutes = startMinutes + (endMinutes - startMinutes)//2

    midTime = [0, 0]
    midTime[0] = midMinutes // 60
    midTime[1] = midMinutes % 60

    return midTime

def printTime(time):
    print('{:02d}:{:02d}'.format(time[0],time[1]))

def main():
    startTimeHours, startTimeMinutes = map(int, input().split(':'))
    endTimeHours, endTimeMinutes = map(int, input().split(':'))

    midTime = getMidTime(startTimeHours, startTimeMinutes, endTimeHours, endTimeMinutes)
    printTime(midTime)

if __name__ == '__main__':
    main()
