

import sys

def main():
    n = int(sys.stdin.readline())
    days = [int(x) for x in sys.stdin.readline().split()]
    days.append(366)
    cleanups = 0
    dirtyness = 0
    for i in range(1, len(days)):
        dirtyness += days[i] - days[i-1]
        if dirtyness >= 20:
            cleanups += 1
            dirtyness -= 20
    print(cleanups)

if __name__ == "__main__":
    main()
