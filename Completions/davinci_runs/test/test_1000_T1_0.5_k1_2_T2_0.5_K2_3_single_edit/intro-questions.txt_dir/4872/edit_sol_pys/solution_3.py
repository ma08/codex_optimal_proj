import sys

def main():
    n = int(sys.stdin.readline())
    dirtyPushes = [int(x) for x in sys.stdin.readline().split()] #[1,2,3,4,5]
    totalDirtiness = 0
    cleanupPhases = 0
    for i in range(n):
        totalDirtiness += (dirtyPushes[i] - i) #5-0, 4-1, 3-2, 2-3, 1-4
        if totalDirtiness >= 20:
            cleanupPhases += 1
            totalDirtiness = 0
    print(cleanupPhases)

if __name__ == "__main__":
    main()
