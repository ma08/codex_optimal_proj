

def main():
    n = int(input())
    dirtyPushes = [int(x) for x in input().split()]

    totalDirtiness = 0
    cleanupPhases = 0
    for i in range(n):
        totalDirtiness += (dirtyPushes[i] - i)
        if totalDirtiness >= 20:
            cleanupPhases += 1
            totalDirtiness = 0
    print(cleanupPhases)

if __name__ == "__main__":
    main()
