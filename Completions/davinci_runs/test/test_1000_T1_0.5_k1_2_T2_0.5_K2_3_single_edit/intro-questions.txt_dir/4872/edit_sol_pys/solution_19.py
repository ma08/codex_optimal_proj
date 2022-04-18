

import sys

def main():
    n = int(sys.stdin.readline())
    days = []
    for i in range(n):
        days.append(int(sys.stdin.readline()))
    days.append(366)
    cleanups = 0
    dirtiness = 0
    for i in range(len(days)-1):
        dirtiness += days[i] - days[i-1]
        if dirtiness >= 20:
            cleanups += 1
            dirtiness = 0
    print(cleanups)

if __name__ == "__main__":
    main()
