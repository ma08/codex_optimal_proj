

import sys

def calcTime(currTime, targetTime):
    #if the difference is greater than 24 hours, subtract 24 hours
    #this will give us the time until the target time
    #calculate the difference between the current time and the target time
    #if the difference is negative, add 24 hours
    #this will give us the time until the target time
    #return the time until the target time
    currTime = currTime.split(':')
    targetTime = targetTime.split(':')
    currTime = [int(currTime[0]), int(currTime[1]), int(currTime[2])]
    targetTime = [int(targetTime[0]), int(targetTime[1]), int(targetTime[2])]
    diff = [targetTime[0] - currTime[0], targetTime[1] - currTime[1], targetTime[2] - currTime[2]]
    diff[0] = diff[0] % 24
    diff[1] = diff[1] % 60
    diff[2] = diff[2] % 60
    return ':'.join(map(str, diff))

def main():
    currTime = sys.stdin.readline().strip()
    targetTime = sys.stdin.readline().strip()
    print(calcTime(currTime, targetTime))

if __name__ == '__main__':
    main()
