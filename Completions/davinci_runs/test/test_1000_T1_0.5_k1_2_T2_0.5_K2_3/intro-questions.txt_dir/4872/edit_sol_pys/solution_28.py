

import sys

def main():
    n = int(sys.stdin.readline())
    days = [int(x) for x in sys.stdin.readline().split()]
    days.append(365)
    cleanups = 0
    dirtyness = 0
    for i in range(len(days)-1):
        dirtyness += days[i] - days[i+1]
        if dirtyness >= 20:
            cleanups += 1
            dirtyness = 0
    print(cleanups)

if __name__ == "__main__":
    main()
