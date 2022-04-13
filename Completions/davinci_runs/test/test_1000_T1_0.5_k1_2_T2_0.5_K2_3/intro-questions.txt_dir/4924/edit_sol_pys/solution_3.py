
import time

def calcTime(currTime, targetTime):
    #if the difference is greater than 24 hours, subtract 24 hours
    #this will give us the time until the target time
    #calculate the difference between the current time and the target time
    #if the difference is negative, add 24 hours
    #this will give us the time until the target time
    #return the time until the target time
    currTime = time.strptime(currTime, '%H:%M:%S')
    targetTime = time.strptime(targetTime, '%H:%M:%S')
    currTime = time.mktime(currTime)
    targetTime = time.mktime(targetTime)
    diff = targetTime - currTime
    if diff < 0:
        diff += 86400
    return time.strftime('%H:%M:%S', time.gmtime(diff))

def main():
    currTime = input()
    targetTime = input()
    print(calcTime(currTime, targetTime))

if __name__ == '__main__':
    main()
