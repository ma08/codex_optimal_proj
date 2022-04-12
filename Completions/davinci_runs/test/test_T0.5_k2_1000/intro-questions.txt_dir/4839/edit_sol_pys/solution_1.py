
def main():
    n = int(input())
    containers = list(map(int, input().split()))
    containers.sort()
    balloons = list(range(1, n + 1)) # balloons = [1, 2, 3, ..., n]
    balloons.sort() # balloons = [1, 2, 3, ..., n]
    balloon_sum = sum(balloons)
    container_sum = sum(containers)
    if container_sum < balloon_sum:
        print('impossible')
        return
    i = 0
    j = 0
    while i < n and j < n:
        if containers[i] >= balloons[j]:
            balloon_sum -= balloons[j]
            container_sum -= containers[i]
            i += 1
            j += 1
        else:
            container_sum -= containers[i]
            i += 1
    if container_sum >= balloon_sum:
        print(balloon_sum / sum(balloons))
    else:
        print('impossible')

if __name__ == "__main__":
    main()
