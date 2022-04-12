

import sys

def calcTime(currTime, targetTime):
    # calculate the difference between the current time and the target time
    # if the difference is negative, add 24 hours
    # this will give us the time until the target time
    # if the difference is greater than 24 hours, subtract 24 hours
    # this will give us the time until the target time
    # return the time until the target time
    currTime = currTime.split(':') # split the current time into hours, minutes, seconds
    targetTime = targetTime.split(':') # split the target time into hours, minutes, seconds
    currTime = [int(currTime[0]), int(currTime[1]), int(currTime[2])] # convert the hours, minutes, seconds to integers
    targetTime = [int(targetTime[0]), int(targetTime[1]), int(targetTime[2])] # convert the hours, minutes, seconds to integers
    diff = [targetTime[0] - currTime[0], targetTime[1] - currTime[1], targetTime[2] - currTime[2]] # calculate the difference between the current time and the target time
    if diff[0] < 0: # if the difference is negative, add 24 hours
        diff[0] += 24 # add 24 hours
    if diff[1] < 0: # if the difference is negative, add 60 minutes
        diff[0] -= 1 # subtract 1 hour
        diff[1] += 60 # add 60 minutes
    if diff[2] < 0: # if the difference is negative, add 60 seconds
        diff[1] -= 1 # subtract 1 minute
        diff[2] += 60 # add 60 seconds
    if diff[0] > 24: # if the difference is greater than 24 hours, subtract 24 hours
        diff[0] -= 24 # subtract 24 hours
    return ':'.join(map(str, diff)) # return the time until the target time

def main():
    currTime = sys.stdin.readline().strip() # read in the current time
    targetTime = sys.stdin.readline().strip() # read in the target time
    print(calcTime(currTime, targetTime)) # print the time until the target time

if __name__ == '__main__':
    main()
