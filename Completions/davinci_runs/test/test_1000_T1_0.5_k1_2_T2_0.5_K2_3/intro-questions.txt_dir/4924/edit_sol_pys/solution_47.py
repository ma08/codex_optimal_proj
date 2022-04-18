
import sys

def calcTime(currTime, targetTime):
    # Calculate the difference between the current time and the target time
    # If the difference is negative, add 24 hours
    # This will give us the time until the target time
    # If the difference is greater than 24 hours, subtract 24 hours
    # This will give us the time until the target time
    # Return the time until the target time
    currTime = [int(currTime.split(':')[0]), int(currTime.split(':')[1]), int(currTime.split(':')[2])]
    targetTime = [int(targetTime.split(':')[0]), int(targetTime.split(':')[1]), int(targetTime.split(':')[2])]
    diff = [targetTime[0] - currTime[0], targetTime[1] - currTime[1], targetTime[2] - currTime[2]]
    if diff[0] < 0:
        diff[0] += 24
    if diff[1] < 0:
        diff[0] -= 1
        diff[1] += 60
    if diff[2] < 0:
        diff[1] -= 1
        diff[2] += 60
    if diff[0] > 24:
        diff[0] -= 24
    return ':'.join(map(str, diff))

def main():
    currTime = sys.stdin.readline().strip()
    targetTime = sys.stdin.readline().strip()
    print(calcTime(currTime, targetTime))

if __name__ == '__main__':
    main()
