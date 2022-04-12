

import sys

def main():
    n = int(sys.stdin.readline())
    days = [int(x) for x in sys.stdin.readline().split()]
    days.append(366) # add a final day to the list
    cleanups = 0
    dirtiness = 1 # the first day is always dirty
    for i in range(len(days)-1):
        dirtiness += days[i] - days[i-1] # add the difference between the days
        if dirtiness >= 20:
            cleanups += 1 # add a cleanup
            dirtiness = 0 # reset the dirtiness
    print(cleanups)

if __name__ == "__main__":
    main()
