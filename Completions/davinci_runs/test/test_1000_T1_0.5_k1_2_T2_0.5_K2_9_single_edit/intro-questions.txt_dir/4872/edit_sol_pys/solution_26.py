

import sys

def main():
    n = int(sys.stdin.readline())
    dirtyPushes = [int(x) for x in sys.stdin.readline().split()] # dirty pushes
    totalDirtiness = 0 # total dirtiness
    cleanupPhases = 0 # cleanup phases
    for i in range(n):
        totalDirtiness += (dirtyPushes[i] - i)
        if totalDirtiness >= 20:
            cleanupPhases += 1
            totalDirtiness = 0
    print(cleanupPhases)

if __name__ == "__main__":
    main()
