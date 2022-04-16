
import sys

def calcTime(currTime, targetTime):
    #calculate the difference between the current time and the target time
    #if the difference is negative, add 24 hours
    #this will give us the time until the target time
    #if the difference is greater than 24 hours, subtract 24 hours
    #this will give us the time until the target time
    #return the time until the target time
    curr_time = currTime.split(':')
    target_time = targetTime.split(':')
    curr_time = [int(curr_time[0]), int(curr_time[1]), int(curr_time[2])]
    target_time = [int(target_time[0]), int(target_time[1]), int(target_time[2])]
    diff = [target_time[0] - curr_time[0], target_time[1] - curr_time[1], target_time[2] - curr_time[2]]
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
    curr_time = sys.stdin.readline().strip()
    target_time = sys.stdin.readline().strip()
    print(calcTime(curr_time, target_time))

if __name__ == '__main__':
    main()
