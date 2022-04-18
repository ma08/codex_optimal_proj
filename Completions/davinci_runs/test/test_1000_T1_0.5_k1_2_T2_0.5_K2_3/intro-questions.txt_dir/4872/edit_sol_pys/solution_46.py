

import sys

def main():
    n = int(sys.stdin.readline())  # number of days
    days = [int(x) for x in sys.stdin.readline().split()]
    days.append(366)  # end of year, day 366
    cleanups = 0
    dirtiness = 0  # amount of dirtiness, starts at 0
    for i in range(1, len(days)):
        dirtiness += days[i] - days[i-1]  # add dirtiness for day
        if dirtiness >= 20:
            cleanups += 1  # add a cleanup
            dirtiness = 0  # reset dirtiness
    print(cleanups)

if __name__ == "__main__":
    main()
