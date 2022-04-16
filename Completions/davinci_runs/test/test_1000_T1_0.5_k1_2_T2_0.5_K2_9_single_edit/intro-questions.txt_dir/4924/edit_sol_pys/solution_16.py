

import sys

def calcTime(currTime, targetTime):
    currTime = currTime.split(':')
    targetTime = targetTime.split(':')
    currTime = [int(currTime[0]), int(currTime[1]), int(currTime[2])]
    targetTime = [int(targetTime[0]), int(targetTime[1]), int(targetTime[2])]
    diff = [0, 0, 0]
    diff[2] = targetTime[2] - currTime[2]
    diff[1] = targetTime[1] - currTime[1]
    diff[0] = targetTime[0] - currTime[0]
    if diff[2] < 0:
        diff[2] += 60
        diff[1] -= 1
    if diff[1] < 0:
        diff[1] += 60
        diff[0] -= 1
    if diff[0] < 0:
        diff[0] += 24
    if diff[0] >= 24:
        diff[0] -= 24
    return '{}:{}:{}'.format(diff[0], diff[1], diff[2])

def main():
    currTime = sys.stdin.readline().strip()
    targetTime = sys.stdin.readline().strip()
    print(calcTime(currTime, targetTime))

if __name__ == '__main__':
    main()
