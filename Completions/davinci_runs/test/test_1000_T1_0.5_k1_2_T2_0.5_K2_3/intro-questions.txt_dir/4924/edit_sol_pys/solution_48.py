

import sys

def calcTime(currTime, targetTime):
    # Calculate the difference between the current time and the target time
    # If the difference is negative, add 24 hours
    # This will give us the time until the target time
    # If the difference is greater than 24 hours, subtract 24 hours
    # This will give us the time until the target time
    # Return the time until the target time
    currTime = currTime.split(':') # Split the current time into hours, minutes, and seconds
    targetTime = targetTime.split(':') # Split the target time into hours, minutes, and seconds
    currTime = [int(currTime[0]), int(currTime[1]), int(currTime[2])] # Convert the current time to integers
    targetTime = [int(targetTime[0]), int(targetTime[1]), int(targetTime[2])] # Convert the target time to integers
    diff = [targetTime[0] - currTime[0], targetTime[1] - currTime[1], targetTime[2] - currTime[2]] # Calculate the difference between the current time and the target time
    if diff[0] < 0: # If the difference in the hour is negative, add 24 hours
        diff[0] += 24 # Add 24 hours
    if diff[1] < 0: # If the difference in the minute is negative, subtract 1 hour and add 60 minutes
        diff[0] -= 1 # Subtract 1 hour
        diff[1] += 60 # Add 60 minutes
    if diff[2] < 0: # If the difference in the second is negative, subtract 1 minute and add 60 seconds
        diff[1] -= 1 # Subtract 1 minute
        diff[2] += 60 # Add 60 seconds
    if diff[0] > 24: # If the difference in the hour is greater than 24 hours, subtract 24 hours
        diff[0] -= 24 # Subtract 24 hours
    return ':'.join(map(str, diff)) # Return the difference in hours, minutes, and seconds

def main():
    currTime = sys.stdin.readline().strip() # Read the current time from stdin
    targetTime = sys.stdin.readline().strip() # Read the target time from stdin
    print(calcTime(currTime, targetTime)) # Calculate the time until the target time

if __name__ == '__main__':
    main()
